"""Generates "Data/s/-2000 tum abilities.erm" and the hatred cfg overrides in "Data/Creatures".

Inputs:
  - crexpbon.txt (original WoG + TUM stack experience table, from ResOunD / Stack Experience Rebalance)
  - ResOunD/Data/Creatures/*.cfg (native hatreds "HateNNNN=value")
  - src/tum upgrade chains.txt (creature -> upgrade pairs, taken from an in-game MA:U dump)

Rules:
  1. Listed abilities of a creature are copied to its TUM upgrade (same stack experience row).
  2. Hatred closure, separately for native (cfg) and stack experience hatreds:
     a creature hates every member of an upgrade chain if it, or a creature it is upgraded from,
     hates any member of that chain. Only pairs with at least one TUM creature (ID >= 197) are
     added, so the original game hatreds stay as they are. A hatred is not added to one system
     when the creature already hates that target in the other system (no double bonus).

Run from the mod folder:  python src/make_tum_abilities.py
"""
import collections
import os
import re

MOD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODS = os.path.dirname(MOD)
CREXPBON = os.path.join(MODS, 'Stack Experience Rebalance', 'Data', 'crexpbon.txt')
RESOUND_CFG = os.path.join(MODS, 'ResOunD', 'Data', 'Creatures')
CHAINS = os.path.join(MOD, 'src', 'tum upgrade chains.txt')
OUT_ERM = os.path.join(MOD, 'Data', 's', '-2000 tum abilities.erm')
OUT_CFG = os.path.join(MOD, 'Data', 'Creatures')

FIRST_TUM = 197
MAX_EXP_TARGET = 255   # stack experience rows store the modifier in one byte
STAT_ROWS = set('HADMmS')
MAX_SLOTS = 20
STAT_SLOTS = 6

# (from, to, row type letter, row modifier) - stack experience rows copied to the TUM upgrade
COPY_ROWS = [
    (45, 214, 'i', '='),    # Winged Magog: No Range Penalty
    (37, 210, 'w', 'B'),    # Arcane Genie: Blind immunity
    (37, 210, 'w', 'H'),    # Arcane Genie: Hypnotize immunity
    (37, 210, 'w', 'K'),    # Arcane Genie: Berserk immunity
    (150, 202, 'W', '+'),   # Seraph: Magic Resistance
    (150, 202, 'w', 'W'),   # Seraph: Water immunity
    (153, 219, 'W', '+'),   # Antichrist: Magic Resistance
    (9, 320, 'r', '#100'),  # High Priest: Regeneration
    (9, 320, 'g', '%'),     # High Priest: Reduced spell damage
    (271, 280, 'f', 'R'),   # Dragon Golem: No Retaliation
    (349, 350, 'f', 'R'),   # Spring Spirit: No Retaliation
    (313, 314, 'L', '#49'), # Centamonth Thrower: Deflect
    (313, 314, 'f', 'D'),   # Centamonth Thrower: Strike Twice
    (103, 244, 'F', '='),   # Catoblepas: Fear
    (93, 236, 'a', '#17'),  # Lightningbird: Lightning Bolt
    (73, 227, 'c', '#73'),  # Harpy Sanguinary: Disease
    (156, 238, 'w', 'B'),   # Spectral Behemoth: Blind immunity
    (15, 293, 'f', 'c'),    # Centaur General: Charge bonus
    (1, 197, 'f', 'f'),     # Royal Halberdier: Fearless
    (79, 229, 's', '#49'),  # Black Minotaur: Expert Mirth
    (99, 321, 's', '#49'),  # Gnoll Shaman: Mirth
    (277, 285, 'p', '#16'), # Abyssal Triton: Ice Bolt
]

# (creature, target) - native hatreds already named in the creature description (no extra text)
HATE_TEXT_EXISTS = {(289, 292), (290, 289), (292, 290)}

# (creature, row type letter, old modifier, new modifier) - existing rows whose modifier is changed
CHANGE_MODIFIER = [
    (217, 'u', '#48', 216),   # Pit Master summons Sharp-Horned Demons instead of Demons
    (259, 'l', '#193', 259),  # Spellweaver clones itself (like Enchanter)
]


# Every native (cfg) hatred added by this script: +100% damage (double damage), from rank 0.
# Native values are plain percents; stack experience hatreds are in 10% units and are kept as they are.
NATIVE_HATE_VALUE = 100


def native_hate_value(ranks):
    return NATIVE_HATE_VALUE


def row_codes(letter, modifier):
    ability = ord(letter)
    mod = int(modifier[1:]) if modifier.startswith('#') else ord(modifier[0])
    return ability, mod


def load_crexpbon():
    rows = collections.defaultdict(list)
    with open(CREXPBON, encoding='latin1') as f:
        for line in f.read().splitlines()[1:]:
            r = line.split('\t')
            if len(r) >= 14 and r[0].isdigit():
                rows[int(r[0])].append(r)
    return rows


def load_cfg():
    cfg = {}
    for name in os.listdir(RESOUND_CFG):
        m = re.fullmatch(r'(\d+)\.cfg', name)
        if m:
            with open(os.path.join(RESOUND_CFG, name), encoding='latin1') as f:
                cfg[int(m.group(1))] = f.read().splitlines()
    return cfg


def load_chains():
    ups = {}
    with open(CHAINS) as f:
        for line in f:
            line = line.split('#')[0].strip()
            if line:
                a, b = map(int, line.split())
                ups[a] = b
    # Standard upgrades that MA:U does not report
    for k in range(0, 112, 2):
        ups.setdefault(k, k + 1)
    for a, b in ((112, 127), (113, 125), (114, 129), (115, 123), (118, 119), (120, 121), (130, 131)):
        ups.setdefault(a, b)
    return ups


def main():
    rows = load_crexpbon()
    cfg = load_cfg()
    ups = load_chains()

    # Chain groups (connected components of upgrade links)
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in ups.items():
        parent[find(a)] = find(b)
    groups = collections.defaultdict(set)
    for x in list(parent):
        groups[find(x)].add(x)
    group = lambda x: groups[find(x)] if x in parent else {x}

    # Creatures a creature is upgraded from (all levels)
    downs = collections.defaultdict(set)
    for a, b in ups.items():
        downs[b].add(a)

    def lower(x):
        seen, todo = set(), [x]
        while todo:
            for p in downs[todo.pop()]:
                if p not in seen and p != x:
                    seen.add(p)
                    todo.append(p)
        return seen

    # Existing hatreds
    exp_hate = collections.defaultdict(dict)   # creature -> target -> ranks
    for mon, rs in rows.items():
        for r in rs:
            if r[1] == 'h' and r[2].startswith('#'):
                exp_hate[mon][int(r[2][1:])] = [int(v) for v in r[3:14]]
    cfg_hate = collections.defaultdict(dict)   # creature -> target -> value
    for mon, lines in cfg.items():
        for line in lines:
            m = re.fullmatch(r'Hate(\d+)=(\d+)', line.strip())
            if m:
                cfg_hate[mon][int(m.group(1))] = int(m.group(2))

    all_mons = set(rows) | set(cfg) | set(parent)

    def closure(hate, other):
        added = collections.defaultdict(dict)
        for h in sorted(all_mons):
            # nearest source first: the creature itself, then the creatures it is upgraded from
            for src in [h] + sorted(lower(h), reverse=True):
                for t0, val in hate.get(src, {}).items():
                    for t in sorted(group(t0)):
                        if t in hate.get(h, {}) or t in added[h] or t in group(h):
                            continue
                        if h < FIRST_TUM and t < FIRST_TUM:
                            continue
                        if t in other.get(h, {}):
                            continue
                        added[h][t] = val
        return added

    # Native hatreds first, stack experience hatreds are then not added where a native one exists
    new_cfg_hate = closure(cfg_hate, exp_hate)
    all_cfg_hate = collections.defaultdict(dict)
    for src in (cfg_hate, new_cfg_hate):
        for h, targets in src.items():
            all_cfg_hate[h].update(targets)
    new_exp_hate = closure(exp_hate, all_cfg_hate)

    # The stack experience table keeps the hatred target in one byte: targets above 255 wrap
    # around to another creature (293 -> 37). Such hatreds become native (cfg) hatreds (see
    # native_hate_value), and the wrong rows of the original table are disabled.
    disable_rows = []   # (creature, ability, stored modifier)
    for h, targets in list(new_exp_hate.items()):
        for t in [t for t in targets if t > MAX_EXP_TARGET]:
            ranks = targets.pop(t)
            if t not in all_cfg_hate.get(h, {}):
                new_cfg_hate[h][t] = native_hate_value(ranks)
    for h, targets in exp_hate.items():
        for t, ranks in targets.items():
            if t > MAX_EXP_TARGET:
                disable_rows.append((h, ord('h'), t % 256))
                if t not in all_cfg_hate.get(h, {}):
                    new_cfg_hate[h][t] = native_hate_value(ranks)

    # Stack experience rows to add
    add_rows = collections.defaultdict(list)   # creature -> [(ability, modifier, ranks, comment)]
    for a, b, letter, modifier in COPY_ROWS:
        src = [r for r in rows[a] if r[1] == letter and r[2] == modifier]
        assert src, (a, letter, modifier)
        ability, mod = row_codes(letter, modifier)
        add_rows[b].append((ability, mod, [int(v) for v in src[0][3:14]],
                            'from %d: %s' % (a, src[0][14].split(':', 1)[-1].strip())))
    for h, targets in new_exp_hate.items():
        for t, ranks in sorted(targets.items()):
            add_rows[h].append((ord('h'), t, ranks, 'hatred %d' % t))

    for a, letter, old, new in CHANGE_MODIFIER:
        assert any(r[1] == letter and r[2] == old for r in rows[a]), (a, letter, old)

    # Slot check
    problems = []
    for mon, add in add_rows.items():
        used = STAT_SLOTS + sum(1 for r in rows.get(mon, []) if r[1] not in STAT_ROWS)
        if used + len(add) > MAX_SLOTS:
            problems.append('%d: %d rows + %d new > %d' % (mon, used, len(add), MAX_SLOTS))

    # ---- ERM ----
    out = []
    w = out.append
    w('ZVSE2')
    w('')
    w('** TUM CREATURE ABILITIES (WoG option 950 "Creature Tweaks")')
    w('** GENERATED by src/make_tum_abilities.py - do not edit by hand.')
    w('**')
    w('** - Third upgrades (Third Upgrade Mod in ResOunD) get stack experience abilities of their')
    w('**   lower upgrade that they were missing (e.g. Winged Magog: No Range Penalty).')
    w('** - Hatreds: a creature hates every member of an upgrade chain if it, or a creature it is')
    w('**   upgraded from, hates any member of it (e.g. Fairy also hates Skeleton Knights).')
    w('**   Native hatreds are in the cfg files of "Data/Creatures" (always active).')
    w('** - Pit Master summons Sharp-Horned Demons, Spellweaver clones itself.')
    w('** Rows go to free stack experience slots, existing abilities are kept.')
    w('')
    w('!#DC(TUMA_OPTION) = 950;')
    w('')
    w('; Finds the slot of a stack experience row (-1 if the creature does not have it).')
    w('; EA:F returns an empty line when the row is not found, so the line is checked.')
    w('!?FU(TUMA_FindRow);')
    w('!#VA(mon:x) (ability:x) (modifier:x) (result:x);')
    w('')
    w('!!VR(result):S-1;')
    w('!!EA(mon):F(ability)/(modifier)/?(slot:y);')
    w('!!FU|(slot)<0/(slot)>19:E;')
    w('!!EA(mon):B(slot)/?(active:y)/?(foundAbility:y)/?(foundModifier:y)/d/d/d/d/d/d/d/d/d/d/d;')
    w('!!VR(result)&(foundAbility)=(ability)/(foundModifier)=(modifier):S(slot);')
    w('')
    w('; Adds a stack experience row to a free slot (6-19), unless the creature already has it.')
    w('!?FU(TUMA_AddRow);')
    w('!#VA(mon:x) (ability:x) (modifier:x) (r0:x) (r1:x) (r2:x) (r3:x) (r4:x) (r5:x) (r6:x) (r7:x) (r8:x) (r9:x) (r10:x);')
    w('')
    w('!!FU(TUMA_FindRow):P(mon)/(ability)/(modifier)/?(existing:y);')
    w('!!FU&(existing)>=0:E;')
    w('')
    w('!!VR(slot:y):S-1;')
    w('!!re k/6/19;')
    w('  !!EA(mon):Bk/?(active:y)/?(oldAbility:y)/d/d/d/d/d/d/d/d/d/d/d/d;')
    w('  !!if|(active)=0/(oldAbility)=0;')
    w('    !!VR(slot):Sk;')
    w('    !!br;')
    w('  !!en;')
    w('!!en;')
    w('')
    w('!!EA(mon)&(slot)>=0:B(slot)/1/(ability)/(modifier)/(r0)/(r1)/(r2)/(r3)/(r4)/(r5)/(r6)/(r7)/(r8)/(r9)/(r10);')
    w('')
    w('; Changes the modifier of an existing stack experience row')
    w('!?FU(TUMA_ChangeModifier);')
    w('!#VA(mon:x) (ability:x) (oldModifier:x) (newModifier:x);')
    w('')
    w('!!FU(TUMA_FindRow):P(mon)/(ability)/(oldModifier)/?(slot:y);')
    w('!!EA(mon)&(slot)>=0:B(slot)/d/d/(newModifier)/d/d/d/d/d/d/d/d/d/d/d;')
    w('')
    w('; Disables a stack experience row')
    w('!?FU(TUMA_DisableRow);')
    w('!#VA(mon:x) (ability:x) (modifier:x);')
    w('')
    w('!!FU(TUMA_FindRow):P(mon)/(ability)/(modifier)/?(slot:y);')
    w('!!EA(mon)&(slot)>=0:B(slot)/0/d/d/d/d/d/d/d/d/d/d/d/d/d;')
    w('')
    w('; Appends "Hates <names>." to the description of a creature. Targets end with -1.')
    w('!?FU(TUMA_AddHateText);')
    w('!#VA(mon:x);')
    w('')
    w('!!VR(names:z):S^^;')
    w('!!re i/2/16;')
    w('  !!br&xi<0;')
    w('  !!SN:H^monname^/xi/1/?(name:z);')
    w('  !!VR(names)&i>2:+^, ^;')
    w('  !!VR(names):+(name);')
    w('!!en;')
    w('')
    w('!!SN:H^monname^/(mon)/2/?(desc:z);')
    w('!!SN:H^monname^/(mon)/2/^%(desc) Hates %(names).^;')
    w('')
    w('; Native hatreds from the cfg files are always active, so their texts are too.')
    w('!?FU(OnAfterErmInited)&i^cr_hasResound^;')
    for mon, targets in sorted(new_cfg_hate.items()):
        ts = sorted(t for t in targets if (mon, t) not in HATE_TEXT_EXISTS)
        if ts:
            assert len(ts) <= 14, mon
            w('!!FU(TUMA_AddHateText):P%d/%s/-1;' % (mon, '/'.join(map(str, ts))))
    w('')
    w('!?FU(OnGameEnter);')
    w('!!UN:P(TUMA_OPTION)/?(enabled:y);')
    w('!!FU&(enabled)<>(TRUE):E;')
    w('!!FU&i^cr_hasResound^<>(TRUE):E;   [needs ResOunD, see "31 forge and fury - dependencies.erm"]')
    w('!!UN:P(WOG_OPT_STACK_EXPERIENCE)/?(stackExp:y);')
    w('!!FU&(stackExp)<>(TRUE):E;')
    w('')
    for a, letter, old, new in CHANGE_MODIFIER:
        ability, mod = row_codes(letter, old)
        w('!!FU(TUMA_ChangeModifier):P%d/%d/%d/%d;' % (a, ability, mod, new))
    w('')
    w('; Hatred rows of the original table whose target ID is above 255 (they hit a wrong creature,')
    w('; the hatred is a native one in "Data/Creatures" instead)')
    for h, ability, mod in sorted(disable_rows):
        w('!!FU(TUMA_DisableRow):P%d/%d/%d;' % (h, ability, mod))
    w('')
    for mon in sorted(add_rows):
        for ability, mod, ranks, comment in add_rows[mon]:
            w('!!FU(TUMA_AddRow):P%d/%d/%d/%s; [%s]' % (mon, ability, mod, '/'.join(map(str, ranks)), comment))
    w('')
    with open(OUT_ERM, 'w', newline='\r\n', encoding='latin1') as f:
        f.write('\n'.join(out))

    # ---- cfg overrides ----
    os.makedirs(OUT_CFG, exist_ok=True)
    for name in os.listdir(OUT_CFG):
        if name.endswith('.cfg'):
            os.remove(os.path.join(OUT_CFG, name))
    for mon, targets in sorted(new_cfg_hate.items()):
        if not targets:
            continue
        lines = [l for l in cfg.get(mon, []) if l.strip()]
        lines += ['Hate%04d=%d' % (t, NATIVE_HATE_VALUE) for t in sorted(targets)]
        with open(os.path.join(OUT_CFG, '%d.cfg' % mon), 'w', newline='\r\n', encoding='latin1') as f:
            f.write('\n'.join(lines) + '\n')

    print('rows added: %d for %d creatures' % (sum(map(len, add_rows.values())), len(add_rows)))
    print('exp hatreds added: %d' % sum(map(len, new_exp_hate.values())))
    print('native hatreds added: %d in %d cfg files' % (sum(map(len, new_cfg_hate.values())),
                                                        sum(1 for t in new_cfg_hate.values() if t)))
    for p in problems:
        print('SLOT PROBLEM', p)


if __name__ == '__main__':
    main()

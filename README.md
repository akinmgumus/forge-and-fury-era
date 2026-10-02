# Forge & Fury

> I have been playing Heroes of Might and Magic III for about 20 years. Over those years I kept thinking "this artifact could be better", "this creature deserves more", "why does this happen?". Forge & Fury is where I finally tried those ideas. It is a hobby project, made for fun and for my own games, and I'm sharing it in case other players enjoy it too. Feedback and bug reports are welcome.

An add-on for **Heroes of Might and Magic III: HoMM 3 ERA** (WoG). It adds:
- new artifacts and combination artifacts,
- two new heroes and a new creature (Dark Phoenix),
- an Attack Speed mechanic,
- creature reworks,
- fixes for several popular ERA mods (ResOunD / Third Upgrade Mod, Advanced Classes Mod, Enhanced Henchmen, Stack Experience Rebalance, Easy Cheats).

Every feature can be switched on or off in **WoG Options → Custom Scripts**. Features that need another mod switch themselves off when that mod is not enabled. Only WoG and the Era Erm Framework are strictly required; the rest is optional.

---

## Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Options](#options)
- [Creature Tweaks (950)](#creature-tweaks-950)
- [Henchmen Tweaks (951)](#henchmen-tweaks-951)
- [New Heroes (953)](#new-heroes-953)
- [Dark Phoenix, a new creature](#dark-phoenix-a-new-creature)
- [Custom Artifacts (955)](#custom-artifacts-955)
- [Attack Speed (996)](#attack-speed-996)
- [Always-on fixes](#always-on-fixes)
- [Recommended settings for other mods](#recommended-settings-for-other-mods)
- [Known issues](#known-issues)
- [For modders](#for-modders)
- [Credits](#credits)

---

## Requirements

**Always required**
- HoMM 3 ERA 3.9 or newer
- WoG, Era Erm Framework

**Per feature**

| Feature | Needs |
|---|---|
| Sharpshooter Rework, golem income, always-on fixes | nothing else |
| Commander Death Stare | Advanced Classes Mod |
| Third-upgrade abilities and hatreds | ResOunD (Third Upgrade Mod), WoG Stack Experience |
| Henchmen Tweaks | Enhanced Henchmen |
| Holika, Aurelius | ResOunD and Advanced Classes Mod |
| Dark Phoenix | ResOunD |
| All new artifacts | ResOunD (the Emerald artifact plugin) |
| Eye of Providence: scouting events and artillery | Advanced Classes Mod (optional; the other bonuses work without it) |
| Attack Speed | ERA Scripts (it replaces that mod's option 996). Game Enhancement Mod is needed for the creature window row |
| Chat fix | Easy Cheats |

The check is automatic. A feature whose mod is missing is switched off, even if its option is ticked.

## Installation
1. **Download:** on GitHub, click **Code → Download ZIP** (or `git clone` the repository).
2. **Extract** it into the game's `Mods` folder and **rename the folder to `Forge and Fury`**. The ZIP from GitHub is named `forge-and-fury-era-main`; the scripts work with any name, but the rest of this README uses `Forge and Fury`.
3. **Install the mods you want to use with it** (see [Requirements](#requirements)). Everything is optional except WoG and the Era Erm Framework.
4. **Enable it** in the ERA Mod Manager and put it at the **top** of the list, above ResOunD, so it has the highest priority. This matters: Forge & Fury replaces some of ResOunD's files.
5. Check [Recommended settings for other mods](#recommended-settings-for-other-mods), especially the Stack Experience Rebalance line-ending fix.
6. Start a **new game** and tick the options you want in WoG Options → Custom Scripts. For Holika and Aurelius also tick **Enable Extension Heroes** (WoG option 100), otherwise they never appear in taverns.

Nothing has to be built: all generated files (archives, sounds, creature configs, scripts) are in the repository. The Python scripts in `src/` are only needed to change them.

**Savegames:** ERA stores scripts inside savegames. After an update, load the save, press **F12** on the adventure map to reload the scripts, then save again. Some features (stack experience tables, creature files) need a new game.

## Options

| Option | Name | Contents |
|---|---|---|
| 950 | Creature Tweaks | Sharpshooter Rework, golem income, commander Death Stare, third-upgrade abilities and hatreds |
| 951 | Henchmen Tweaks | Obstacle-free start hex, henchman growth |
| 953 | New Heroes | Holika (Tower) and Aurelius (Conflux) |
| 955 | Custom Artifacts | Pegasus Harness, Minerjack, Wealth of Erebus, Eye of Providence, Lightning Boots, Svalinn set |
| 996 | Attack Speed | Replaces ERA Scripts' "Gnolls Marauders Strike First" |

---

## Creature Tweaks (950)

### Sharpshooter Rework
- **Upgrade chain:** Sharpshooter → Arctic Sharpshooter ↔ Lava Sharpshooter.
  - Available in the Hill Fort, or in town with Universal Creature Upgrades.
  - Arctic and Lava cost 800 gold, so Sharpshooter → Arctic costs 400 per creature.
  - Switching between Arctic and Lava is free.

| | Attack | Defense | Damage | HP |
|---|---|---|---|---|
| Arctic Sharpshooter | Sharpshooter +2 | Sharpshooter +5 | 11-13 | 20 |
| Lava Sharpshooter | Sharpshooter +5 | Sharpshooter +2 | 14 | 20 |

- **Arctic:** casts Slow on the target after a shot, if the target survives.
- **Lava:** after a shot, Fire Walls burn on the targeted hex and its 6 neighbours (7 hexes, obstacles skipped).
  - Fire Wall power = number of Lava Sharpshooters / 10 (at least 1).
- **Chance:** 10% per stack experience rank, so 100% at rank 10.
- Stack experience stat bonuses still apply.
- Settings are at the top of `Data/s/-2000 sharpshooter rework.erm`.

### Golem income
Each Gold Golem gives 10 gold per day and each Diamond Golem 20 gold per day. This counts heroes' armies and town garrisons.

### Stat changes (needs ResOunD)
- **Antichrist** deals a fixed 75 damage (ResOunD: 55-65).

### Commander Death Stare (needs Advanced Classes Mod)
Advanced Classes Mod replaces the commanders' Death Stare with Poison. With this option they have both:
- The ability text is changed.
- The icon is the Death Stare icon from WoG Graphics Fix.

### Third-upgrade abilities (needs ResOunD)
The Third Upgrade Mod creatures in ResOunD sometimes miss stack experience abilities that their lower upgrade has. They now get them, with the same values and ranks:

| Third upgrade | Added (from the lower upgrade) |
|---|---|
| Winged Magog | No Range Penalty |
| Arcane Genie | Blind, Hypnotize and Berserk immunity |
| Seraph | Magic Resistance, Water immunity |
| Antichrist | Magic Resistance |
| High Priest | Regeneration, reduced spell damage |
| Dragon Golem, Spring Spirit | No Retaliation |
| Centamonth Thrower | Deflect, Strike Twice |
| Catoblepas | Fear |
| Lightningbird | Lightning Bolt (keeps Chain Lightning) |
| Harpy Sanguinary | Disease (keeps Curse) |
| Spectral Behemoth | Blind immunity |
| Centaur General | Charge Bonus |
| Royal Halberdier | Fearless |
| Black Minotaur | Expert Mirth |
| Gnoll Shaman | Mirth |
| Abyssal Triton | Ice Bolt |

- **Pit Master** summons Sharp-Horned Demons instead of Demons.
- **Spellweaver** summons clones of itself, like the Enchanter does.

### Hatreds (needs ResOunD)
- If a creature, or a creature it upgrades from, hates any member of an upgrade chain, it now hates **every** member of that chain. For example, Fairies also hate Skeleton Knights, and Tiamat hates every Rampart dragon.
- Only pairs with at least one Third Upgrade Mod creature are added, so the original game hatreds stay as they are.
- **Bug fix:** the stack experience table stores the hated creature's ID in one byte. Hatreds against creatures with an ID above 255 hit a wrong creature: for example, Dire Werewolves had a bonus against **Archangels** instead of Light Templars. This applied to 34 hatreds in the original tables. They are disabled and re-added as native hatreds, which have no such limit.
- **Native hatreds** added by this mod (shown as "Hates …" in the creature description) give **+100% damage**, from rank 0.
- Stack experience hatreds keep their original values (up to +200% at rank 10).

---

## Henchmen Tweaks (951)
Needs Enhanced Henchmen.
- **Clear start hex:** an obstacle on a henchman's starting hex(es) is removed before the henchman is placed.
- **Growth:** after every 10 battles won with a living henchman, its quantity grows by 5% (at least +1).
  - With Diplomacy the growth is 5% + 5% per level: Basic 10%, Advanced 15%, Expert 20%, Master 25%, Grandmaster 30%.
  - The quantity returns to 1 if the henchman is replaced or dismissed.
  - In battle the quantity is capped at double the base.
- Settings are at the top of `Data/s/-2000 henchmen growth.erm`.

## New Heroes (953)
Needs ResOunD and Advanced Classes Mod. Each new hero gives an upgrade that no town building can give.

### Holika (Tower)
- The campaign hero Mutare (slot 151) becomes **Holika**, a female Alchemist (Tower).
- **Commander:** a Temple Guardian named Raktabija.
- **Availability:** like Dracon and Gelu, she can't be chosen at game start, but she can appear in taverns when "Enable Extension Heroes" (WoG option 100) is on.
- **Specialty:** she upgrades the Naga Rakshasas in her army to **Asuras** anywhere, like Gelu does with Sharpshooters. The cost is the price difference (2600 gold + 2 gems per creature by default).
- Naga specialists (Fafner) also improve Asuras.
- **Start:** Tactics and Learning, a spell book with Magic Arrow, and Gremlins, Gargoyles and Golems.
- New portraits and a new specialty icon.

### Aurelius (Conflux)
- The campaign hero Roland (slot 152) becomes **Aurelius**, a male Planeswalker (Conflux): a knight burned in phoenix fire and reborn in the Conflux in a black flame.
- **Commander:** an Astral Spirit named Vesper.
- **Availability:** as Holika.
- **Specialty:** he evolves the Divine Phoenixes in his army into **Dark Phoenixes** anywhere. The cost is the price difference.
- **Start:** Offense and Leadership, Sprites and two of Air, Water and Fire Elementals (chosen at random).
- New portraits and a new specialty icon.

## Dark Phoenix, a new creature
Needs ResOunD. A level 6 Conflux creature in the unused creature slot 122, the evolution of the Divine Phoenix (only through Aurelius; it is never generated on the map).

| Attack | Defense | Damage | HP | Speed | Attack Speed | Cost |
|---|---|---|---|---|---|---|
| 40 | 38 | 60-75 | 700 | 24 | 10 | 12 000 gold + 7 mercury |

- Keeps the Divine Phoenix's abilities: fire immunity, Rebirth, Regeneration, Fire Shield and its stack experience.
- **Fear** and **Death Stare**: 10% per creature at rank 0, +3% per stack experience rank (40% at rank 10). Living creatures only.
- **Black Flame:** a stack hit by a Dark Phoenix can't be healed, resurrected or reborn for the rest of the battle.
- **Stack experience:** Strike and Return (rank 5), No Retaliation (rank 7), 5% less spell damage per rank (50% at rank 10), one more Rebirth at rank 5 and two at rank 10.
- Black-and-white Phoenix animation and portraits, built by `src/make_dark_phoenix.py`.
- TrainerX: shown on an extra page after the last creature page.

## Custom Artifacts (955)
Needs ResOunD (Emerald). All new artifacts are Relics.

**Combining:**
- Artifacts with IDs above 170 can't be parts in the game's own combination system, so some combinations are made by the script.
  - When all parts are equipped and you close the hero screen, the game asks whether to combine them.
  - If you answer No, it asks again after a part is re-equipped.
  - AI players combine automatically.
- When parts are combined, their own bonuses (and the Advanced Classes Mod set bonuses of the parts) are replaced by the new artifact's bonuses.
- The price of a combination is always the sum of its parts, except for Eye of Providence.

### Pegasus Harness (neck, 20 000)
Necklace of Swiftness + Ring of the Wayfarer + Cape of Velocity.
- All units: +4 speed, +1 minimum and maximum damage, Expert Air Shield for 50 rounds.
- Slowest unit: +5 speed on top of that.
- 10% chance to fully avoid melee or ranged damage.
- War machines and towers are excluded.

### Minerjack (misc, 10 000)
Inexhaustible Cart of Ore + Inexhaustible Cart of Lumber.
- +10 Wood and +10 Ore per day, equipped or in the backpack.

### Wealth of Erebus (misc, 30 000)
Minerjack + Cornucopia (a combination of two combination artifacts, combined by the script).
- +10 Wood, Ore, Mercury, Sulfur, Crystal and Gems and +2 Mithril per day.
- After defeating another player's hero, 10% of one of that player's resources is transferred to you.

### Eye of Providence (misc, 10 000)
Speculum + Spyglass.
- Scouting radius +5.
- On the first day of every week, a radius-30 area around the hero is revealed.
- +1 to all primary skills.
- With Advanced Classes Mod:
  - Pre-battle artillery damage multiplier +5.
  - More frequent scouting events, and the "ACM Reward" event is never cancelled.
- "Prepare for Battle" at the start of every battle: a random bonus to all units (Attack, Defense, Health or Speed, scaling with hero level).

### Lightning Boots (feet, 9 000)
Equestrian's Gloves + Boots of Speed. Only while equipped:
- +1000 land movement points.
- +1 speed for all creatures in battle.
- **Grandmaster Logistics:** a hero with lower or no Logistics gets Expert Logistics + Master + Grandmaster (Advanced Classes Mod). The hero's own level comes back when the boots are removed. This needs a free skill slot.

### Svalinn set
Four new artifacts. They can appear on the map. Combined by the script:

| Artifact | Slot | Price | Bonus |
|---|---|---|---|
| Frostbite Axe | right hand | 15 000 | +3 Attack; Frost |
| Helm of the Jarl | head | 8 000 | +3 Defense, +3 Knowledge |
| Berserker's Byrnie | torso | 6 000 | +1 Attack, +1 Defense, +3 Knowledge |
| Shield of Jormungandr | left hand | 15 000 | +7 Defense, +4 Spell Power, +1 Knowledge; Venom |
| **Svalinn** (all four) | left hand | 44 000 | +4 Attack, +11 Defense, +4 Spell Power, +7 Knowledge; Frost, Venom, Fire Ward |

- **Frost:**
  - An enemy that makes a melee attack on your stack (not a retaliation) gets Expert Slow for 3 rounds. Immunity and resistance apply.
  - Your melee attacks have a 15% chance to prevent retaliation.
- **Venom:** all enemy stacks are poisoned for 50 rounds at the start of battle.
- **Fire Ward:** your stacks are immune to the enemy's harmful Fire spells and to Fire Wall / Land Mine damage. Your own helpful Fire spells still work. Magic Arrow is not blocked.
- With Attack Speed on: -1 Attack Speed for all enemy stacks.

---

## Attack Speed (996)
Needs ERA Scripts. It uses that mod's option 996 and its first-strike mechanism.

**How it works**
- Every creature has an **Attack Speed** from 1 to 10. The table is in `src/attack speed values.md`.
- In a melee attack, if the defender's Attack Speed is **higher** than the attacker's, the defender strikes first. If it is equal or lower, the normal order is used.
- There is no first strike when:
  - the attacker has "no enemy retaliation",
  - the attacker is a war machine,
  - the defender has no retaliation left,
  - the defender is blinded, petrified or paralyzed.

**Modifiers**

| Source | Change |
|---|---|
| Cavaliers, Champions, Holy Champions | Full value when charging; half when attacking an adjacent enemy or defending |
| Slow | -1 (Expert: -2) |
| Haste | +1 (Expert: +2) |
| Svalinn | -1 for enemy stacks |

The minimum is 1, and there is no upper limit.

**Creature window** (needs Game Enhancement Mod)
- A new row above Speed shows "Attack Speed 7", or "7(5)" when modified, or "8/4" for cavalry.
- In battle, Health shows "max(left)".

---

## Always-on fixes
- **Obstacle removal crash:** removing a battlefield obstacle freed its graphic even when other obstacles still used it, which crashed the game a few moves later. Forge & Fury' own obstacle removal (Lava Sharpshooter, henchman start hex) keeps the graphic alive. See `CR_RemoveObstacleSafe` in `-2000 fixes.erm`.
- **Savegame load crash (WoG Mithril bug):** WoG adds Mithril to `Mithril[owner of the hero]` without checking that the owner is a valid player (0-7). With a wrong owner the amount is written far behind that array, into WoG's custom hero portrait table. When it lands on the "used" field of an entry, every savegame made afterwards crashes while loading (`Hd_wog`, inside `LoadPcx8`). `EraPlugins/AfterWoG/forge and fury - wog fixes.bin` adds the missing owner check in both places and makes the loader skip portraits with an empty name, so already damaged saves load again. `-2000 fixes.erm` also clears damaged entries on game enter.
- **First Aid Tent errors (Advanced Classes Mod):** in a battle that is resolved without the battle screen (a quick battle chosen for one fight, or a battle replayed while a savegame loads), ACM's First Aid Tent code caused a series of "Attempt to use !!BM in non-human battle" error windows. `30 acm fixes - pre.erm` skips that code outside real, visible battles.
- **Damage:** creatures whose minimum damage is higher than their maximum get the two values swapped.
- **Stack experience damage bonus:** creatures with equal minimum and maximum damage get the same bonus on both, so "5-4" rounding errors no longer appear.
- **Spellweaver animation fix:** `cr259.def`.
- **Chat fix (Easy Cheats):** Easy Cheats reads every chat line that is not a cheat as an ERM command or variable, so normal text such as "Death Stare" caused an ERM error window. Normal text is now cleared before Easy Cheats reads it; cheats, ERM commands and variable dumps still work. An empty chat line no longer causes an error either.
- **Tavern:** every hero class has weight 20 in its own town's tavern and 5 elsewhere (`hctraits.txt`). This change is not tied to an option.

## Recommended settings for other mods
- **Stack Experience Rebalance:**
  - Its `Data/crexpbon.txt` is shipped with Unix line endings, so WoG reads no stack experience abilities at all: every creature shows only stat bonuses. Convert the file to Windows (CRLF) line endings; its content is the same as ResOunD's table.
  - Its "WoG/TUM Abilities" and "Neutrals" switches remove all original stack experience abilities and give every creature a single new one. To keep the original abilities (which this mod builds on), set these in `Runtime/stack experience rebalance.ini`:
    ```
    Exp_WoG_Abilities=0
    Exp_WoG_Neutrals=0
    Exp_TUM_Abilities=0
    Exp_TUM_Neutrals=0
    ```
    The stat growth settings still work.
- **JS - map generation fixes:** in our tests it crashed during random map generation together with ResOunD.
- **JS - main module:** its `JS_BugFixes.era` (together with an empty `artefact merchant fix.dll` that switches off WoG's own fix) shifted the artifacts in the Artifact Merchants "sell" screen in our setup with Game Enhancement Mod. Renaming both files in `JS - main module/EraPlugins` (e.g. adding `.off`) brings WoG's fix back.

## Known issues
- Holika's and Aurelius' texts (specialty, commander biography) replace Mutare's and Roland's texts even when option 953 is off.
- The tavern weights (`hctraits.txt`) are always active.
- Native hatreds and the Dark Phoenix (`Data/Creatures/*.cfg`) are always active, because the game reads creature files before options exist.
- `Data/forge and fury creatures.pac` replaces ResOunD's creature tables (`zcrtrait.txt`, `cranim.txt`) to add the Dark Phoenix row. If ResOunD updates those tables, run `python src/make_dark_phoenix.py` again.
- The Emerald artifact archive (`Data/EmeraldArtifacts.pac`) is a copy of ResOunD's archive with the new artifacts added. If ResOunD updates that archive, Forge & Fury has to be updated too.

## For modders
- Scripts are in `Data/s`:
  - The `-2000` prefix loads them after all other mods.
  - The `30` / `31` prefixes load them before other mods (for handlers that must run first).
- `31 forge and fury - dependencies.erm` sets `i^cr_hasResound^`, `i^cr_hasACM^`, `i^cr_hasHenchmen^`, `i^cr_hasEraScripts^` and `i^cr_hasEasyCheats^`.
- Generated files (do not edit them by hand):

| Output | Source | Command |
|---|---|---|
| `-2000 attack speed table.erm` | `src/attack speed values.md` | `python src/make_attack_speed_table.py` |
| `-2000 tum abilities.erm`, `Data/Creatures/*.cfg` | settings at the top of the generator script | `python src/make_tum_abilities.py` |
| `Data/forge and fury creatures.pac`, `Data/forge and fury.snd`, `Data/Creatures/122.cfg`, Dark Phoenix portraits | ResOunD's files (needs ResOunD installed and Pillow) | `python src/make_dark_phoenix.py` |

- Stack experience notes:
  - `EA:F` returns an empty line, not -1, when an ability is not found.
  - Ability rows keep their modifier in one byte (0-255).
- Artifact IDs used: 280-289. The next free ID is 290 and the next free combination slot is 27.
- `src/` has the editable text tables, icon sources and generators.

## Credits
Forge & Fury by **akinm**.

It builds on, and patches files of, these mods:
- **ResOunD / Third Upgrade Mod**: VMaiko, PerryR, Archer30 (with the Emerald and Amethyst plugins). `Data/EmeraldArtifacts.pac`, `Data/Creatures/*.cfg` and `Data/forge and fury creatures.pac` (Dark Phoenix animation recolored from ResOunD's Phoenix, Divine Phoenix sounds, creature tables) are modified copies of ResOunD files.
- **Advanced Classes Mod**: PerryR
- **Stack Experience Rebalance**: PerryR
- **Enhanced Henchmen**: Archer30
- **ERA Scripts**: Algor, Archer30
- **Game Enhancement Mod**: daemon_n. The creature window background is a modified copy.
- **WoG Graphics Fix**: Grossmaster. The Death Stare icons are copied from it.
- **Era, Era Erm Framework, Easy Cheats**: Berserker
- **In The Wake Of Gods**: the WoG Team

All rights to the original files belong to their authors.

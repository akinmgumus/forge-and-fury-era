"""Builds the Dark Phoenix: a black-and-white recolor of the Phoenix, in the unused creature slot 122.

Why slot 122: adding creature 358 (raising Amethyst's creature count) crashed every creature
dialog and battle - other plugins keep fixed-size per-creature data. Slots 122/124/126/128
("NOT USED") are inside the original creature range, and the game's own table names their files
"bad1".."bad4" (def and sound prefix), so the new files only need those names.

Outputs (in the mod folder):
  Data/forge and fury creatures.pac   (Forge & Fury is above ResOunD in the mod list, so these files
                    are found before ResOunD's AmeCre.pac):
      bad1             battle animation (ResOunD's Cphx.def with a new palette)
      zcrtrait.txt, Crtraits.txt, CRTRAIT0.txt   ResOunD's creature table, row "NOT USED (1)" replaced
      cranim.txt       ResOunD's animation timing table, row 122 replaced (Phoenix timings)
  Data/forge and fury.snd                 BAD1ATTK/DFND/KILL/MOVE/WNCE (Phoenix sounds)
  Data/Creatures/122.cfg                  Amethyst creature config
  Data/forge and fury.zip                 portrait pngs (twcrport.def/0_124.png, cprsmall.def/0_124.png)

The recolor ("G"): the brightest flame parts become white, everything else deep black.
Palette indices 0-7 (transparency, shadow, selection) are kept.

Run from the mod folder:  python src/make_dark_phoenix.py
The game must be closed (the archives are locked while it runs).
"""
import io
import os
import struct
import sys
import zipfile
import zlib

from PIL import Image

MOD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODS = os.path.dirname(MOD)
GAME = os.path.dirname(MODS)
RESOUND = os.path.join(MODS, 'ResOunD', 'Data')

# The creature starts as a copy of the Divine Phoenix (sounds, Amethyst config; stats and stack
# experience are copied by "-2000 dark phoenix.erm") with the black portraits.
# MODE 'divine': also the Divine Phoenix animation (unchanged).
# MODE 'dark':   the black-and-white Phoenix animation.
MODE = 'dark'

NEW_ID = 122                       # unused slot "NOT USED (1)"
FILE_NAME = 'bad1'                 # def name and sound prefix of slot 122 in the game's creature table
BASE_ID = 131                      # Phoenix
PORTRAIT_FRAME = NEW_ID + 2        # portrait def frame = creature id + 2
BASE_PORTRAIT_FRAME = BASE_ID + 2

NAME, PLURAL = 'Dark Phoenix', 'Dark Phoenixes'
# Draft stats (to be tuned): Wood Mercury Ore Sulfur Crystal Gems Gold, FightValue AIValue Growth Horde,
# HP Speed Attack Defense DmgLow DmgHigh Shots Spells AdvLow AdvHigh
STATS = [0, 2, 0, 0, 0, 0, 12000, 38500, 50000, 1, 0, 700, 24, 40, 38, 60, 75, 0, 2, 1, 3]
DESCRIPTION = 'Fire spell immunity. Rebirth.'
# Added to the Divine Phoenix config (Amethyst keys, see ResOunD/AmeEditGuide.pdf):
#   Fear=1            10% chance that an enemy stack skips its turn
#   Attack effect=2   Death Stare (0 vampire, 1 thunder, 2 death stare, 3 dispel, 4 acid)
#   DoNotGenerate=1   never placed on maps (only Roland's evolution makes it)
EXTRA_CFG = ['Fear=1', 'Attack effect=2', 'DoNotGenerate=1']

# Flags as the Phoenix: double wide, flying, breath attack, king 1, fire immunity, no morale
CFG = ['Flags=147595', 'Level=6', 'Town=8', 'Fearless=1',
       'rebirth chance=1.000000', 'rebirth fraction=0.300000', 'rebirth sure=0.200000']


# ---------------------------------------------------------------- archives
def lod_entries(path):
    d = open(path, 'rb').read()
    n = struct.unpack_from('<I', d, 8)[0]
    out = {}
    for i in range(n):
        o = 92 + 32 * i
        name = d[o:o + 16].split(b'\0')[0].decode('latin1')
        off, size, _typ, csize = struct.unpack_from('<IIII', d, o + 16)
        raw = d[off:off + (csize or size)]
        out[name.lower()] = (name, zlib.decompress(raw) if csize else raw)
    return out


def lod_read(path, name):
    e = lod_entries(path).get(name.lower())
    return e[1] if e else None


def write_lod(path, files):
    # The game finds files with a binary search: the index must be sorted by lower-case name.
    files = sorted(files, key=lambda f: f[0].lower())
    hdr = b'LOD\0' + struct.pack('<II', 200, len(files)) + b'\0' * 80
    off = 92 + 32 * len(files)
    table = b''
    data = b''
    for name, raw in files:
        c = zlib.compress(raw, 9)
        table += name.encode('latin1').ljust(16, b'\0') + struct.pack('<IIII', off + len(data), len(raw), 0, len(c))
        data += c
    tmp = path + '.new'
    open(tmp, 'wb').write(hdr + table + data)
    for name, raw in files:
        assert lod_read(tmp, name) == raw
    os.replace(tmp, path)


def write_amecre(path, src, files):
    """Copies ResOunD's AmeCre.pac (entries kept byte for byte) and replaces/adds files."""
    d = open(src, 'rb').read()
    n = struct.unpack_from('<I', d, 8)[0]
    new = {name.lower(): (name, raw) for name, raw in files}
    entries = []
    for i in range(n):
        o = 92 + 32 * i
        name = d[o:o + 16].split(b'\0')[0].decode('latin1')
        off, size, typ, cs = struct.unpack_from('<IIII', d, o + 16)
        if name.lower() in new:
            raw = new.pop(name.lower())[1]
            blob = zlib.compress(raw, 9)
            entries.append((name, len(raw), typ, len(blob), blob))
        else:
            entries.append((name, size, typ, cs, d[off:off + (cs or size)]))
    for name, raw in new.values():
        blob = zlib.compress(raw, 9)
        entries.append((name, len(raw), 0, len(blob), blob))
    # The game finds files with a binary search: the index must be sorted by lower-case name.
    entries.sort(key=lambda e: e[0].lower())
    base = 92 + 32 * len(entries)
    table = b''
    body = bytearray()
    for name, size, typ, cs, blob in entries:
        table += name.encode('latin1').ljust(16, b'\0') + struct.pack('<IIII', base + len(body), size, typ, cs)
        body += blob
    tmp = path + '.new'
    open(tmp, 'wb').write(d[:8] + struct.pack('<I', len(entries)) + d[12:92] + table + bytes(body))
    for name, raw in files:
        assert lod_read(tmp, name) == raw
    os.replace(tmp, path)


def snd_entries(path):
    d = open(path, 'rb').read()
    n = struct.unpack_from('<I', d, 0)[0]
    out = {}
    for i in range(n):
        o = 4 + 48 * i
        name = d[o:o + 40].split(b'\0')[0].decode('latin1')
        off, size = struct.unpack_from('<II', d, o + 40)
        out[name.upper()] = d[off:off + size]
    return out


def write_snd(path, files):
    off = 4 + 48 * len(files)
    table = b''
    data = b''
    for name, raw in files:
        table += name.encode('latin1').ljust(40, b'\0') + struct.pack('<II', off + len(data), len(raw))
        data += raw
    tmp = path + '.new'
    open(tmp, 'wb').write(struct.pack('<I', len(files)) + table + data)
    os.replace(tmp, path)


# ---------------------------------------------------------------- recolor
def lum(r, g, b):
    return (0.299 * r + 0.587 * g + 0.114 * b) / 255


def recolor(r, g, b):
    """Variant G: white flame tips (brightest parts), deep black everything else."""
    L = lum(r, g, b)
    if L > 0.74:
        t = min(1.0, (L - 0.74) / 0.15)
        v = round(170 + 85 * t)
    else:
        v = round((L / 0.74) ** 2.6 * 28)
    v = max(0, min(255, v))
    return v, v, v


def recolor_def_palette(d):
    pal = bytearray(d[16:16 + 768])
    for i in range(8, 256):
        pal[i * 3:i * 3 + 3] = bytes(recolor(*pal[i * 3:i * 3 + 3]))
    return d[:16] + bytes(pal) + d[16 + 768:]


def rename_def_frames(d, old_prefix, new_prefix):
    """Gives every frame a new name (old_prefix -> new_prefix, extension .pcx).

    Frames are shared between defs by name: with the Phoenix's frame names the new def got
    the Phoenix's frame objects and its creature dialogs crashed.
    """
    d = bytearray(d)
    _t, _w, _h, g = struct.unpack_from('<IIII', d, 0)
    o = 16 + 768
    for _ in range(g):
        _gid, cnt, _u1, _u2 = struct.unpack_from('<IIII', d, o)
        o += 16
        for i in range(cnt):
            p = o + 13 * i
            name = bytes(d[p:p + 13]).split(b'\0')[0].decode('latin1')
            stem = name.rsplit('.', 1)[0]
            assert stem.lower().startswith(old_prefix), name
            new = (new_prefix + stem[len(old_prefix):] + '.pcx').encode('latin1')
            assert len(new) <= 12, new
            d[p:p + 13] = new.ljust(13, b'\0')
        o += 17 * cnt
    return bytes(d)


# ---------------------------------------------------------------- def frames
def def_frames(d):
    """Single-group def: returns (gid, count, u1, u2, names, offsets, header end)."""
    o = 16 + 768
    gid, cnt, u1, u2 = struct.unpack_from('<IIII', d, o)
    no = o + 16
    names = [d[no + 13 * i:no + 13 * i + 13] for i in range(cnt)]
    offs = list(struct.unpack_from('<%dI' % cnt, d, no + 13 * cnt))
    return gid, cnt, u1, u2, names, offs, no + 17 * cnt


def append_copy_of_frame(d, src_index, new_name):
    """Appends a copy of frame src_index (same picture data) as the last frame of a single-group def."""
    t, w, h, g = struct.unpack_from('<IIII', d, 0)
    assert g == 1
    gid, cnt, u1, u2, names, offs, hdr_end = def_frames(d)
    srt = sorted(set(offs))
    i = srt.index(offs[src_index])
    end = srt[i + 1] if i + 1 < len(srt) else len(d)
    blob = d[offs[src_index]:end]
    body = d[hdr_end:]
    delta = 17
    out = bytearray(struct.pack('<IIII', t, w, h, g) + d[16:16 + 768] + struct.pack('<IIII', gid, cnt + 1, u1, u2))
    out += b''.join(names) + new_name.encode('latin1').ljust(13, b'\0')
    out += struct.pack('<%dI' % (cnt + 1), *([x + delta for x in offs] + [hdr_end + delta + len(body)]))
    return bytes(out) + body + blob


def decode_frame(d, idx):
    """Decodes frame idx of a single-group def into an RGBA image (indices 0-7 transparent)."""
    pal = d[16:16 + 768]
    _gid, _cnt, _u1, _u2, _names, offs, _end = def_frames(d)
    off = offs[idx]
    size, fmt, fw, fh, ww, hh, left, top = struct.unpack_from('<IIIIIIii', d, off)
    p = off + 32
    px = bytearray(fw * fh)

    def put(y, x, bs):
        px[(top + y) * fw + left + x:(top + y) * fw + left + x + len(bs)] = bs

    if fmt == 0:
        for y in range(hh):
            put(y, 0, d[p + y * ww:p + (y + 1) * ww])
    elif fmt == 1:
        ro = struct.unpack_from('<%dI' % hh, d, p)
        for y in range(hh):
            q = p + ro[y]
            x = 0
            while x < ww:
                c, n = d[q], d[q + 1] + 1
                q += 2
                if c == 0xFF:
                    put(y, x, d[q:q + n])
                    q += n
                else:
                    put(y, x, bytes([c]) * n)
                x += n
    else:
        ro = struct.unpack_from('<%dH' % hh, d, p)
        for y in range(hh):
            q = p + ro[y]
            x = 0
            while x < ww:
                b = d[q]
                q += 1
                c, n = b >> 5, (b & 31) + 1
                if c == 7:
                    put(y, x, d[q:q + n])
                    q += n
                else:
                    put(y, x, bytes([c]) * n)
                x += n
    img = Image.new('RGBA', (fw, fh))
    rgba = []
    for v in px:
        if v < 8:
            rgba.append((0, 0, 0, 0))
        else:
            rgba.append(tuple(pal[v * 3:v * 3 + 3]) + (255,))
    img.putdata(rgba)
    return img


def warm(r, g, b):
    """Fire colors (red-orange-yellow): the Phoenix itself, not the Conflux background."""
    import colorsys
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
    h *= 360
    return (h <= 65 or h >= 330) and s > 0.30 and v > 0.12


def recolored_png(img):
    """Portrait png: fully opaque, only the fire-colored pixels (the bird) are recolored."""
    out = Image.new('RGBA', img.size)
    out.putdata([(*recolor(r, g, b), 255) if warm(r, g, b) else (r, g, b, 255) for r, g, b, _a in img.getdata()])
    buf = io.BytesIO()
    out.save(buf, 'PNG')
    return buf.getvalue()


# ---------------------------------------------------------------- tables
def replace_line(text, match, new_line):
    """Replaces the first line for which match(line) is true."""
    lines = text.split('\r\n')
    idx = next(i for i, l in enumerate(lines) if match(l))
    lines[idx] = new_line
    return '\r\n'.join(lines)


def main():
    amecre = os.path.join(RESOUND, 'AmeCre.pac')

    files = []
    if MODE == 'divine':
        files.append((FILE_NAME, rename_def_frames(lod_read(amecre, 'CR252.def'), 'zphx', 'yphx')))
    else:
        files.append((FILE_NAME, rename_def_frames(recolor_def_palette(lod_read(amecre, 'Cphx.def')), 'cphx', 'dphx')))

    pngs = {}
    for defname in ('twcrport.def', 'cprsmall.def'):
        d = lod_read(amecre, defname)
        pngs['Data/Defs/%s/0_%d.png' % (defname, PORTRAIT_FRAME)] = recolored_png(decode_frame(d, BASE_PORTRAIT_FRAME))

    row = '\t'.join([NAME, PLURAL] + [str(v) for v in STATS] + [DESCRIPTION, ''])
    table = lod_read(amecre, 'zcrtrait.txt').decode('latin1')
    table = replace_line(table, lambda l: l.startswith('NOT USED (1)\t'), row).encode('latin1')
    for name in ('zcrtrait.txt', 'Crtraits.txt', 'CRTRAIT0.txt'):
        files.append((name, table))

    # cranim.txt: slot 122 is the first "NOT USED" row after the Magic Elemental
    anim = lod_read(amecre, 'cranim.txt').decode('latin1').split('\r\n')
    phx_row = next(l for l in anim if l.endswith('\tPheonix'))
    magic = next(i for i, l in enumerate(anim) if l.endswith('\tMagic Elemental'))
    assert anim[magic + 1].endswith('\tNOT USED'), anim[magic + 1]
    anim[magic + 1] = phx_row[:-len('Pheonix')] + NAME
    files.append(('cranim.txt', '\r\n'.join(anim).encode('latin1')))

    write_lod(os.path.join(MOD, 'Data', 'forge and fury creatures.pac'), files)

    snd = snd_entries(os.path.join(RESOUND, 'AmeCre.snd'))
    sounds = [('%s%s' % (FILE_NAME.upper(), k), snd['S252' + k]) for k in ('ATTK', 'DFND', 'KILL', 'MOVE', 'SHOT', 'WNCE')]
    write_snd(os.path.join(MOD, 'Data', 'forge and fury.snd'), sounds)

    os.makedirs(os.path.join(MOD, 'Data', 'Creatures'), exist_ok=True)
    cfg = [l.strip() for l in open(os.path.join(RESOUND, 'Creatures', '252.cfg'), encoding='latin1') if l.strip()]
    keys = {l.split('=', 1)[0] for l in EXTRA_CFG}
    cfg = [l for l in cfg if l.split('=', 1)[0] not in keys] + EXTRA_CFG
    with open(os.path.join(MOD, 'Data', 'Creatures', '%d.cfg' % NEW_ID), 'w', newline='\r\n') as f:
        f.write('\n'.join(cfg) + '\n')

    # files of the earlier attempt with creature 358
    # (Data/AmeCre.pac: the earlier 57 MB copy of ResOunD's archive, no longer needed)
    for old in (os.path.join('Data', 'amethyst.cfg'), os.path.join('Data', 'Creatures', '358.cfg'),
                os.path.join('Data', 'AmeCre.pac')):
        if os.path.exists(os.path.join(MOD, old)):
            os.remove(os.path.join(MOD, old))
    for old in [n for n in zipfile.ZipFile(os.path.join(MOD, 'Data', 'forge and fury.zip')).namelist() if n.endswith('/0_360.png')]:
        pngs.setdefault(old, None)

    zpath = os.path.join(MOD, 'Data', 'forge and fury.zip')
    tmp = zpath + '.new'
    with zipfile.ZipFile(zpath) as zin, zipfile.ZipFile(tmp, 'w') as zout:
        for it in zin.infolist():
            if it.filename not in pngs:
                zout.writestr(it, zin.read(it.filename))
        for name, raw in pngs.items():
            if raw is not None:            # None = remove (left over from the 358 attempt)
                zout.writestr(zipfile.ZipInfo(name, date_time=(2026, 10, 2, 0, 0, 0)), raw)
    os.replace(tmp, zpath)

    print('pac:', [n for n, _ in files])
    print('snd:', [n for n, _ in sounds])
    print('zip:', [n for n, r in pngs.items() if r is not None])


if __name__ == '__main__':
    main()

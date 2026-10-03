"""Builds the Training skill icons (replacing Nobility, skill 5) from src/training icons/*.png.

Source images (1024x1024): 1 basic.png .. 5 grandmaster.png.
Output: png replacements in Data/forge and fury.zip:
  SECSK82.def (82x93), Secskill.def (44x44), SECSK32.def (32x32): frames 18, 19, 20 (Basic, Advanced,
      Expert) and 97, 98 (Master, Grandmaster of Advanced Classes Mod)
  m_sskills.def frame 5 and sskills.def frame 28 (20x20, one icon per skill): the Expert picture
  H1skills.def frames 5 and 33 (TrainerX skill table, 44x44, colour and grey): the Expert picture

Run from the mod folder:  python src/make_training_icons.py   (the game must be closed)
"""
import io
import os
import zipfile

from PIL import Image

MOD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(MOD, 'src', 'training icons')
ZIP = os.path.join(MOD, 'Data', 'forge and fury.zip')

LEVELS = ['1 basic', '2 advanced', '3 expert', '4 master', '5 grandmaster']
FRAMES = [18, 19, 20, 97, 98]

# crop boxes in the 1024x1024 source: the large icon keeps some of the leather frame (as the ACM
# icons), the small ones show the painted scene, the tiny ones only the swords and the shield
BOX_82x93 = (130, 80, 894, 948)      # 764 x 868 = 82:93
BOX_SQUARE = (150, 150, 874, 874)
BOX_TINY = (240, 230, 784, 774)


def png(img):
    buf = io.BytesIO()
    img.save(buf, 'PNG')
    return buf.getvalue()


def icon(src, box, size):
    return src.crop(box).resize(size, Image.LANCZOS)


def trainer_icons(color):
    """TrainerX's skill table (H1skills.def in Trainer.pac, 44x44): frame 5 in colour and frame 33
    in TrainerX's grey striped style. The stripes are copied from TrainerX's own frame 33."""
    import sys
    import numpy as np
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import make_dark_phoenix as m

    pac = os.path.join(os.path.dirname(MOD), 'TrainerX', 'Data', 'Trainer.pac')
    out = {'Data/Defs/H1skills.def/0_5.png': png(color)}
    if not os.path.exists(pac):
        return out
    d = m.lod_read(pac, 'H1skills.def')

    def frame(idx):
        return np.array(m.decode_frame(d, idx).convert('RGB')).astype(int)

    greys = np.stack([frame(k) for k in range(28, 56)])
    g33 = greys[33 - 28]
    stripes = (np.abs(greys - greys[0]).sum(-1) == 0).all(0)   # identical in all grey frames = stripes
    c = np.array(color).astype(int)
    lum = c[..., 0] * 0.299 + c[..., 1] * 0.587 + c[..., 2] * 0.114
    lum = (lum - lum.min()) * 255 / max(1, lum.max() - lum.min())   # our picture is darker than the originals
    grey = np.clip(lum * 0.6 + 40, 0, 255)
    g = np.stack([grey] * 3, -1)
    g[stripes] = g33[stripes]
    out['Data/Defs/H1skills.def/0_33.png'] = png(Image.fromarray(g.astype('uint8')))
    return out


def main():
    files = {}
    for level, frame in zip(LEVELS, FRAMES):
        src = Image.open(os.path.join(SRC, level + '.png')).convert('RGB')
        files['Data/Defs/SECSK82.def/0_%d.png' % frame] = png(icon(src, BOX_82x93, (82, 93)))
        files['Data/Defs/Secskill.def/0_%d.png' % frame] = png(icon(src, BOX_SQUARE, (44, 44)))
        files['Data/Defs/SECSK32.def/0_%d.png' % frame] = png(icon(src, BOX_SQUARE, (32, 32)))
        if level == '3 expert':
            tiny = png(icon(src, BOX_TINY, (20, 20)))
            files['Data/Defs/m_sskills.def/0_5.png'] = tiny
            files['Data/Defs/sskills.def/0_28.png'] = tiny
            files.update(trainer_icons(icon(src, BOX_SQUARE, (44, 44))))

    tmp = ZIP + '.new'
    with zipfile.ZipFile(ZIP) as zin, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for it in zin.infolist():
            if it.filename not in files:
                zout.writestr(it, zin.read(it.filename))
        for name, raw in files.items():
            zout.writestr(name, raw)
    os.replace(tmp, ZIP)
    print('zip:', sorted(files))


if __name__ == '__main__':
    main()

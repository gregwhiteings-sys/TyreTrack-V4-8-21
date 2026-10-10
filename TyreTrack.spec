# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path
from PyInstaller.utils.hooks import collect_all, collect_submodules

root = Path(SPECPATH)
datas = []
binaries = []
hiddenimports = []
for package in ('ultralytics', 'torch', 'torchvision', 'depthai'):
    d, b, h = collect_all(package)
    datas += d
    binaries += b
    hiddenimports += h

# Keep model outside the exe for easy model updates.
a = Analysis(
    [str(root / 'TyreTrack_V4_8_2_overlay_options.py')],
    pathex=[str(root)],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    excludes=['tensorflow', 'jax', 'cupy', 'torch._dynamo.backends.cudagraphs'],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True,
          name='TyreTrack', debug=False, bootloader_ignore_signals=False,
          strip=False, upx=False, console=False)
coll = COLLECT(exe, a.binaries, a.datas, strip=False, upx=False, name='TyreTrack')

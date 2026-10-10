# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path
from PyInstaller.utils.hooks import collect_all, collect_submodules

root = Path(SPECPATH)
datas, binaries, hiddenimports = [], [], []
for package in ('ultralytics', 'torch', 'torchvision', 'depthai', 'scipy'):
    d, b, h = collect_all(package)
    datas += d
    binaries += b
    hiddenimports += h
# scipy's compiled private helpers may be imported dynamically by tracking.
hiddenimports += collect_submodules('scipy._lib')
hiddenimports += ['scipy._cyutility', 'scipy._lib._ccallback_c']
hiddenimports = sorted(set(hiddenimports))

a = Analysis(
    [str(root / 'TyreTrack_V4_8_2_overlay_options.py')],
    pathex=[str(root)], binaries=binaries, datas=datas,
    hiddenimports=hiddenimports,
    excludes=['tensorflow', 'jax', 'cupy', 'torch._dynamo.backends.cudagraphs'],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True,
          name='TyreTrack', debug=False, bootloader_ignore_signals=False,
          strip=False, upx=False, console=False)
coll = COLLECT(exe, a.binaries, a.datas, strip=False, upx=False, name='TyreTrack')

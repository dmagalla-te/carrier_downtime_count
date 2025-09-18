# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main_endpoint.py'],
    pathex=[],
    binaries=[],
    datas=[('config', 'config')],
    hiddenimports=['httpx', 'pydantic', 'asyncio', 'csv', 're', 'datetime', 'time'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='carrier_downtime_count',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
app = BUNDLE(
    exe,
    name='carrier_downtime_count.app',
    icon=None,
    bundle_identifier=None,
)

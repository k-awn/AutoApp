# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Final-Product\\main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['PySide6', 'selenium', 'undetected-chromedriver', 'sys', 'pyautogui', 'keyboard', 'selenium.webdriver', 'selenium.webdriver.chrome.service', 'selenium.webdriver.common.keys', 'selenium.webdriver.common.by', 'selenium.webdriver.support.ui', 'selenium.webdriver.support.expected_conditions'],
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
    [],
    exclude_binaries=True,
    name='AutoApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['Final-Product\\AppLogo.ico'],
    contents_directory='.',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='AutoApp',
)

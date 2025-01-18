# -*- mode: python ; coding: utf-8 -*-

import os
import shutil
import os
from PyInstaller.utils.hooks import collect_data_files


# Analysis
a = Analysis(
    ['C:/Projekti/UPNBuddit/main.py'],  # Your main Python script
    pathex=[],                          # Optional path for additional modules if required
    binaries=[],                        # Optional binaries
    datas=[],                           # No data files included here, we handle them later
    hiddenimports=[],                  # Hidden imports if needed
    hookspath=[],                      # Optional paths for custom hooks
    hooksconfig={},                    # Custom hooks configuration if required
    runtime_hooks=[],                  # Runtime hooks if needed
    excludes=[],                       # Exclude any specific modules
    noarchive=False,                   # Whether to store Python bytecode in a compressed archive
)

# Create pyz
pyz = PYZ(a.pure)

# Create EXE
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='UPNBuddit',
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
)

# Collect files
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='UPNBuddit',
)

# Move your additional files manually after the build
shutil.copyfile('config.xls', r'{0}\config.xls'.format(coll.name))  # Copy config.xls
shutil.copyfile('seznam.xls', r'{0}\seznam.xls'.format(coll.name))  # Copy seznam.xls
shutil.copytree('templates', r'{0}\templates'.format(coll.name))   # Copy templates folder
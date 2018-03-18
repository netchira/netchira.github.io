# -*- coding: utf-8 -*-
from cx_Freeze import setup, Executable


# ----------------------------------------------------------------
# ��{���
# ----------------------------------------------------------------
name = "CompareTxt"
version = "1.0.0"
description = "Compare two txt files, and detect the differences"
author = "netchira"
url = "https://netchira.github.io/"
icon = "icons/favicon.ico"

# �A�v���P�[�V�����̎�ʂ��ȉ�����I��
#  CUI : None
#  GUI : 'Win32GUI'
base = 'Win32GUI'

# UUID�͈�x���߂���ύX���Ȃ�
upgrade_code = "{f0fa6467-ebeb-4576-9fe6-f511dda08a12}"

# ----------------------------------------------------------------
# �Z�b�g�A�b�v����
# ----------------------------------------------------------------
shortcut_table = [
    ('DesktopShortcut',          # Shortcut
     'DesktopFolder',            # Directory_
     "CompareTxt",               # Name
     'TARGETDIR',                # Component_
     '[TARGETDIR]CompareTxt.exe',# Target
     None,                       # Arguments
     None,                       # Description
     None,                       # Hotkey
     None,                       # Icon
     None,                       # IconIndex
     None,                       # ShowCmd
     'TARGETDIR',                # WkDir
    )
    ]

# Table dictionary
msi_data = {'Shortcut': shortcut_table}

# �ǉ����W���[���ŕK�v�Ȃ��̂� packages �ɓ����
build_exe_options = {'packages': [],
                     'excludes': [],
                     'includes': [],
                     'include_files': ["icons/"]
}

bdist_msi_options = {'upgrade_code': upgrade_code,
                     'add_to_path': False,
                     'data': msi_data
}

options = {
    'build_exe': build_exe_options,
    'bdist_msi': bdist_msi_options
}


# exe �ɂ����� python �t�@�C�����w��
script = "CompareTxt.py"
targetName = "CompareTxt.exe"
exe = Executable(script=script,
                 targetName=targetName,
                 base=base,
                 icon=icon
                 )

# �Z�b�g�A�b�v����
setup(name=name,
      version=version,
      author=author,
      url=url,
      description=description,
      options=options,
      executables=[exe]
      )
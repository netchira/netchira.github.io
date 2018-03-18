from distutils.core import setup
import py2exe

# 設定内容
script = 'CompareTxt.py'
option = {
    'compressed': 1,
    'optimize': 2,
    'bundle_files': 3,
}

# セットアップ処理
setup(
    options = {
        'py2exe': option,
    },
    console = [
        {'script': script }
    ],
    zipfile = None,
)
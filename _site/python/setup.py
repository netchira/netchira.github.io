from distutils.core import setup
import py2exe

# �ݒ���e
script = 'CompareTxt.py'
option = {
    'compressed': 1,
    'optimize': 2,
    'bundle_files': 3,
}

# �Z�b�g�A�b�v����
setup(
    options = {
        'py2exe': option,
    },
    console = [
        {'script': script }
    ],
    zipfile = None,
)
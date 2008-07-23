from py2exe.build_exe import py2exe
from distutils.core import setup

opts = {
    "py2exe": {
        "includes": ["sip"],
        "packages": ["qgis","PyQt4"],
        "dist_dir": "bin",
    }
}

setup(options = opts,
      windows=[{"script": "openoceanmap.py"}] )

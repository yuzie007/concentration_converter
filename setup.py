#!/usr/bin/env python
from distutils.core import setup

packages = [
    'concentration_converter',
]
scripts = [
    'scripts/at2wt',
    'scripts/wt2at',
]
__version__ = '0.0.0'
setup(name='concentration_converter',
      version=__version__,
      author="Yuji Ikeda",
      author_email="y.ikeda@mpie.de",
      packages=packages,
      scripts=scripts)

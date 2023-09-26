#!/usr/bin/env python

"""
setup.py file for SWIG lgpio
"""

from setuptools import setup, Extension
import glob

with open('README.md') as f:
    long_description = f.read()

sources = glob.glob("../lg*.c")
sources.append('../rgpiod.c')
sources.append('lgpio.i')


lgpio_module = Extension('_lgpio', sources=sources, libraries=['rt', 'dl'], extra_compile_args=['-I../', '-pthread'])

setup (name = 'lgpio',
       version = '0.2.2.0',
       zip_safe=False,
       author='joan',
       author_email='joan@abyz.me.uk',
       maintainer='joan',
       maintainer_email='joan@abyz.me.uk',
       url='http://abyz.me.uk/lg/py_lgpio.html',
       description='Linux SBC GPIO module',
       long_description=long_description,
       long_description_content_type="text/markdown",
       download_url='http://abyz.me.uk/lg/lg.zip',
       license='unlicense.org',
       keywords=['linux', 'sbc', 'gpio',],
       classifiers=[
         "Programming Language :: Python :: 2",
         "Programming Language :: Python :: 3",
       ],
       ext_modules = [lgpio_module],
       py_modules = ["lgpio"],
       )


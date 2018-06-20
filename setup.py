#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import dirname, realpath, exists
from setuptools import setup
import sys


author = u"Paul Müller"
authors = ["Philipp Rosendahl", author]
name = 'fcswrite'
description = 'Write .fcs files (flow cytometry)'
year = "2016"

long_description = """
This package provides basic functionalities for writing flow cytometry
standard (.fcs) files.
"""

sys.path.insert(0, realpath(dirname(__file__)) + "/" + name)
from _version import version


if sys.version_info[0]==2:
    # Note:
    # scipy and matplotlib<1.3.0 are required for fcm
    # To be able to use matplotlib>1.3.0, we monkeypatch
    # matplotlib for fcm.
    # fcm only seems to work with Python 2.
    tests_require = ["fcm", "mock"]
    install_pathlib = ["pathlib"]
else:
    tests_require = []
    install_pathlib = []


setup(
    name=name,
    author=author,
    author_email='dev@craban.de',
    url='http://ZELLMECHANIK-DRESDEN.github.io/fcswrite/',
    version=version,
    packages=[name],
    package_dir={name: name},
    license="BSD (3 clause)",
    description=description,
    long_description=open('README.rst').read() if exists('README.rst') else '',
    install_requires=["numpy>=1.7.0"]+install_pathlib,
    setup_requires=['pytest-runner'],
    tests_require=["pytest"]+tests_require,
    include_package_data=True,
    keywords=["fcs", "flow cytometry", "flow cytometry standard"],
    classifiers= [
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research'
                 ],
    platforms=['ALL'],
    )

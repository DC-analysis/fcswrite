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

sys.path.insert(0, realpath(dirname(__file__))+"/"+name)
from _version import version

if __name__ == "__main__":
    setup(
        name=name,
        author=author,
        author_email='paul.mueller at biotec.tu-dresden.de',
        url='http://ZELLMECHANIK-DRESDEN.github.io/fcswrite/',
        version=version,
        packages=[name],
        package_dir={name: name},
        license="BSD (3 clause)",
        description=description,
        long_description=open('README.rst').read() if exists('README.rst') else '',
        install_requires=["NumPy>=1.7.0"],
        setup_requires=['pytest-runner'],
        tests_require=["pytest",
                       "fcm",
                       # fcm requires matplotlib.nxutils which was removed
                       # in matplotlib version 1.3.0:
                       # http://matplotlib.org/1.3.0/api/api_changes.html
                       "matplotlib==1.1.0"
                       ],
        keywords=["fcs", "flow cytometry", "flow cytometry standard"],
        classifiers= [
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Intended Audience :: Science/Research'
                     ],
        platforms=['ALL'],
        )

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
from _version import version  # noqa: E402


setup(
    name=name,
    author=author,
    author_email='dev@craban.de',
    url='https://github.com/ZELLMECHANIK-DRESDEN/fcswrite',
    version=version,
    packages=[name],
    package_dir={name: name},
    license="BSD (3 clause)",
    description=description,
    long_description=open('README.rst').read() if exists('README.rst') else '',
    install_requires=["numpy>=1.7.0",
                      ],
    setup_requires=['pytest-runner'],
    python_requires=">=3.6",
    tests_require=["pytest",
                   "fcsparser",
                   ],
    include_package_data=True,
    keywords=["fcs", "flow cytometry", "flow cytometry standard"],
    classifiers=['Operating System :: OS Independent',
                 'Programming Language :: Python :: 3',
                 'Topic :: Scientific/Engineering :: Visualization',
                 'Intended Audience :: Science/Research',
                 ],
    platforms=['ALL'],
    )

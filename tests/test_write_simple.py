#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import numpy as np
import os
from os.path import join, dirname, abspath, split
import pytest
import sys
import tempfile

# Add parent directory to beginning of path variable
DIR = dirname(abspath(__file__))
sys.path.insert(0, split(DIR)[0])

import fcswrite


def test_write_fcs():
    """test that fcm can read the data files"""
    fname=tempfile.mktemp(suffix=".fcs", prefix="write_test")
    data = 1.0*np.arange(400).reshape((100,4))
    chn_names= ['cha', 'chb', 'ch3', 'ch4']
    fcswrite.write_fcs(filename=fname,
                       chn_names=chn_names,
                       data=data
                       )

    with open(fname, "rb") as fd:
        data = fd.read()
    data = np.frombuffer(data, dtype=np.uint16)
    # remove empty lines
    data = data[data != 8224]
    data = data.tostring()
    hasher = hashlib.md5()
    hasher.update(data)
    hexval=hasher.hexdigest()
    assert hexval == "bbb090b99ccb1c9b1d8b43b83eddc7d3"
    os.remove(fname)


if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()
    

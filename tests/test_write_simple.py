#!/usr/bin/env python
# -*- coding: utf-8 -*-
import md5
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
    hasher = md5.md5()
    with open(fname, "rb") as fd:
        # Remove empty spaces
        # Maybe the empty characters will be changed in a future
        # file format. This could cause this test to fail.
        data = fd.read().replace(" ", "")
    hasher.update(data)
    hexval=hasher.hexdigest()
    assert hexval == "086539803c3a8479e33d0e059d1ef8c9"
    os.remove(fname)


if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()
    

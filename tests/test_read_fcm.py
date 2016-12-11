#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fcm import loadFCS
import numpy as np
import os
from os.path import join, dirname, abspath, split
import sys
import tempfile

# Add parent directory to beginning of path variable
DIR = dirname(abspath(__file__))
sys.path.insert(0, split(DIR)[0])

import fcswrite


def test_read_fcm():
    """test that fcm can read the data files"""
    fname=tempfile.mktemp(suffix=".fcs", prefix="fcm_read_test")
    data = 1.0*np.arange(400).reshape((100,4))
    chn_names= ['c1', 'channel_2', 'Channel 3', '4jjjjjjjjj']
    fcswrite.write_fcs(filename=fname,
                       chn_names=chn_names,
                       data=data,
                       compat_chn_names=False
                       )

    
    ldata = loadFCS(fname)
    assert ldata.shape == data.shape
    assert ldata.channels == chn_names
    assert np.mean(ldata) == np.mean(data)
    assert np.all(ldata == data)
    os.remove(fname)


if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()
    

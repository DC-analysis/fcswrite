#!/usr/bin/env python
# -*- coding: utf-8 -*-
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


@pytest.mark.skipif("sys.version_info >= (3,0)")
def test_read_fcm():
    """test that fcm can read the data files"""
    # fix for fcm, which does not support matplotlib>=1.3.0
    from mock import patch, MagicMock
    module_mock = MagicMock()

    with patch.dict('sys.modules', **{ 
            'matplotlib.nxutils': module_mock,
            'matplotlib.nxutils.points_inside_poly': module_mock,
        }):
        from fcm import loadFCS

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
    

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib
import tempfile

import fcswrite
import fcsparser
import numpy as np


def test_read_fcsparser():
    """test that fcm can read the data files"""
    fname = tempfile.mktemp(suffix=".fcs", prefix="fcm_read_test")
    fpath = pathlib.Path(fname)
    data = 1.0*np.arange(400).reshape((100, 4))
    chn_names = ['c1', 'channel_2', 'Channel 3', '4jjjjjjjjj']
    fcswrite.write_fcs(filename=fpath,
                       chn_names=chn_names,
                       data=data,
                       compat_chn_names=False
                       )

    meta, ldata = fcsparser.parse(fname)
    assert meta["fcswrite version"] == fcswrite.__version__
    assert ldata.shape == data.shape
    assert list(ldata.columns) == chn_names
    assert np.mean(ldata.values) == np.mean(data)
    assert np.all(ldata .values == data)
    try:
        fpath.unlink()
    except OSError:
        pass


def test_read_fcm_99999999():
    """
    test that fcm can read data with data segments ending
    beyond the 99,999,999th byte

    This test creates a 160MB temporary file.
    """
    fname = tempfile.mktemp(suffix=".fcs", prefix="fcm_read_test")
    fpath = pathlib.Path(fname)
    data = 1.0*np.linspace(1, 100, 40000000).reshape((10000000, 4))
    chn_names = ['ch1', 'ch2', 'ch3', 'ch4']
    fcswrite.write_fcs(filename=fpath,
                       chn_names=chn_names,
                       data=data,
                       compat_chn_names=False
                       )

    _, ldata = fcsparser.parse(fname)
    assert ldata.shape == data.shape
    assert list(ldata.columns) == chn_names
    assert np.allclose(ldata.values, data, atol=0, rtol=1e-7)
    try:
        fpath.unlink()
    except OSError:
        pass


if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pathlib
import tempfile

import numpy as np
import pytest

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

        fname = tempfile.mktemp(suffix=".fcs", prefix="fcm_read_test")
        fpath = pathlib.Path(fname)
        data = 1.0*np.arange(400).reshape((100, 4))
        chn_names = ['c1', 'channel_2', 'Channel 3', '4jjjjjjjjj']
        fcswrite.write_fcs(filename=fpath,
                           chn_names=chn_names,
                           data=data,
                           compat_chn_names=False
                           )

        ldata = loadFCS(fname)
        assert ldata.shape == data.shape
        assert ldata.channels == chn_names
        assert np.mean(ldata) == np.mean(data)
        assert np.all(ldata == data)
        try:
            fpath.unlink()
        except OSError:
            pass


@pytest.mark.skipif("sys.version_info >= (3,0)")
def test_read_fcm_99999999():
    """
    test that fcm can read data with data segments ending
    beyond the 99,999,999th byte

    This test creates a 160MB temporary file.
    """
    # fix for fcm, which does not support matplotlib>=1.3.0
    from mock import patch, MagicMock
    module_mock = MagicMock()

    with patch.dict('sys.modules', **{
        'matplotlib.nxutils': module_mock,
        'matplotlib.nxutils.points_inside_poly': module_mock,
    }):
        from fcm import loadFCS

        fname = tempfile.mktemp(suffix=".fcs", prefix="fcm_read_test")
        fpath = pathlib.Path(fname)
        data = 1.0*np.linspace(1, 100, 40000000).reshape((10000000, 4))
        chn_names = ['ch1', 'ch2', 'ch3', 'ch4']
        fcswrite.write_fcs(filename=fpath,
                           chn_names=chn_names,
                           data=data,
                           compat_chn_names=False
                           )

        ldata = loadFCS(fname)
        assert ldata.shape == data.shape
        assert ldata.channels == chn_names
        assert np.allclose(ldata, data, atol=0, rtol=1e-7)
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

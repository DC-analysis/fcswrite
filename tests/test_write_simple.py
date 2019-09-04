#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import os
import tempfile

import numpy as np

import fcswrite


def test_write_fcs():
    """test that fcm can read the data files"""
    fname = tempfile.mktemp(suffix=".fcs", prefix="write_test")
    data = 1.0*np.arange(400).reshape((100, 4))
    chn_names = ['cha', 'chb', 'ch3', 'ch4']
    # monkey-patch fcswrite version to have reproducible result
    oldver = fcswrite.__version__
    fcswrite.fcswrite.version = "0.5.0"
    fcswrite.write_fcs(filename=fname,
                       chn_names=chn_names,
                       data=data
                       )
    # write back correct version
    fcswrite.fcswrite.version = oldver
    with open(fname, "rb") as fd:
        data = fd.read()
    data = np.frombuffer(data, dtype=np.uint8)
    # remove empty lines
    data = data[data != 8224]
    data = data.tostring()
    hasher = hashlib.md5()
    hasher.update(data)
    hexval = hasher.hexdigest()
    assert hexval == "2b4fdb7012b0693285c31aa91c606216"
    os.remove(fname)


if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()

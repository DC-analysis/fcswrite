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
    fcswrite.write_fcs(filename=fname,
                       chn_names=chn_names,
                       data=data
                       )

    with open(fname, "rb") as fd:
        data = fd.read()
    data = np.frombuffer(data, dtype=np.uint8)
    # remove empty lines
    data = data[data != 8224]
    data = data.tostring()
    hasher = hashlib.md5()
    hasher.update(data)
    hexval = hasher.hexdigest()
    assert hexval == "68ddd6a1494a3374a3c3ebc0b6bbc5ec"
    os.remove(fname)


if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()

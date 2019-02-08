"""Tests for large header sizes

https://github.com/ZELLMECHANIK-DRESDEN/fcswrite/issues/4
"""
import os
import tempfile

import numpy as np

import fcswrite


def test_long_column_names():
    path = tempfile.mktemp(suffix=".fcs", prefix="fcswrite_long_header_")
    n_cols = 500
    chn_names = ["column_name_{:05d}".format(ii) for ii in range(n_cols)]
    data = np.random.randn(1000, n_cols)

    fcswrite.write_fcs(filename=path,
                       chn_names=chn_names,
                       data=data)

    # The HEADER segment byte positions are hard-coded for the FCS3.0 file
    # format.
    with open(path, "rb") as fd:
        data = fd.read()
    end_text = int(data[18:26])
    begin_data = int(data[26:34])

    assert end_text < begin_data

    os.remove(path)


if __name__ == "__main__":
    # Run all tests
    loc = locals()
    for key in list(loc.keys()):
        if key.startswith("test_") and hasattr(loc[key], "__call__"):
            loc[key]()

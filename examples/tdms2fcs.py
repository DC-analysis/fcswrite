#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Convert a tdms file to an fcs file using nptdms and fcswrite

(requires nptdms>=0.23.0)
"""
import nptdms
import numpy as np
from os.path import dirname, abspath, join

import fcswrite


def read_tdms(tdms_file):
    """Read tdms file and return channel names and data"""
    tdms_file = nptdms.TdmsFile(tdms_file)
    ch_names = []
    ch_data = []

    for ch in tdms_file.groups()[0].channels():
        if ch.data is not None and len(ch.data):
            chn = ch.name
            if "unit_string" in ch.properties:
                unit = ch.properties["unit_string"]
                ch_names.append("{} [{}]".format(chn, unit))
            else:
                ch_names.append(chn)

            ch_data.append(ch.data)

    return ch_names, ch_data


def add_deformation(chn_names, data):
    """From circularity, compute the deformation

    This method is useful for RT-DC data sets that contain
    the circularity but not the deformation.
    """
    if "deformation" not in chn_names:
        for ii, ch in enumerate(chn_names):
            if ch == "circularity":
                chn_names.append("deformation")
                data.append(1-data[ii])

    return chn_names, data


def tdms2fcs(tdms_file):
    """Creates an fcs file for a given tdms file"""
    fcs_file = tdms_file[:-4]+"fcs"
    chn_names, data = read_tdms(tdms_file)
    chn_names, data = add_deformation(chn_names, data)
    fcswrite.write_fcs(filename=fcs_file,
                       chn_names=chn_names,
                       data=np.array(data).transpose())


if __name__ == "__main__":
    # Create an fcs file where this tdms file is located:
    tdms_file = join(dirname(abspath(__file__)), "data/example_rt-dc.tdms")
    tdms2fcs(tdms_file)

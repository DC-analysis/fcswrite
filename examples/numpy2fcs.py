#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Write a numpy array to an .fcs file
"""
import numpy as np

import fcswrite


data = 1.0*np.arange(400).reshape((100, 4))
chn_names = ['c1', 'channel_2', 'Channel 3', '4jjjjjjjjj']
fcswrite.write_fcs(filename="my_fcs_file.fcs",
                   chn_names=chn_names,
                   data=data)

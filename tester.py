#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import dataread as dr
from plot_input import prompt_headers

DATA = dr.phantom_evdata('energy_ccc.ev')

[Y, lab, keys] = prompt_headers(DATA.keys(),Ncurves)
# -*- coding: utf-8 -*-
"""
-----------------------------------------------
# File: test.py
# This file is created by Chuanting Zhang
# Email: chuanting.zhang@kaust.edu.sa
# Date: 2020-12-08 (YYYY-MM-DD)
-----------------------------------------------
"""
import numpy as np


def gini_coef(wealths):
    cum_wealths = np.cumsum(sorted(np.append(wealths, 0)))
    sum_wealths = cum_wealths[-1]
    xarray = np.array(range(0, len(cum_wealths))) / np.float(len(cum_wealths)-1)
    yarray = cum_wealths / sum_wealths
    B = np.trapz(yarray, x=xarray)
    A = 0.5 - B
    return A / (A+B)

money = [1, 10, 2, 8, 4, 120]
print(gini_coef(money))
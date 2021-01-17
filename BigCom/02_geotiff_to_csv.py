# -*- coding: utf-8 -*-
"""
-----------------------------------------------
# File: 02_geotiff_to_csv.py
# This file is created by Chuanting Zhang
# Email: chuanting.zhang@kaust.edu.sa
# Date: 2020-12-07 (YYYY-MM-DD)
-----------------------------------------------
"""
from raster2xyz.raster2xyz import Raster2xyz

input_raster = 'd:/sau_ppp_2020_UNadj_constrained.tif'
output_file = 'd:/ksa_tif.csv';

rtxyz = Raster2xyz()
rtxyz.translate(input_raster, output_file)
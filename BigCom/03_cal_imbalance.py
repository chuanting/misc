# -*- coding: utf-8 -*-
"""
-----------------------------------------------
# File: 03_cal_imbalance.py
# This file is created by Chuanting Zhang
# Email: chuanting.zhang@kaust.edu.sa
# Date: 2020-12-08 (YYYY-MM-DD)
-----------------------------------------------
"""
import pandas as pd
import json
import geopandas as gpd
import numpy as np

folder = 'D:/Dataset/HighResolutionPopulation/'
country = 'Uganda'
pop_file = folder + country + '/pop.csv'
bs_file = folder + country + '/BS.csv'
poly_file = folder + country + '/poly/poly.shp'
grid_file = folder + country + '/grid.geojson'

print('Loading population, bs, poly, and grid data...')
df_pop = pd.read_csv(pop_file)
df_bs = pd.read_csv(bs_file)
gdf_poly = gpd.read_file(poly_file)
gdf_poly.set_crs('epsg:4326', inplace=True)
grid = json.load(open(grid_file))
print('Creating GeoDataFrame from grid data...')
df_grid = gpd.GeoDataFrame.from_features(grid['features'])
df_grid['id'] = range(df_grid.shape[0])
df_grid.set_crs('epsg:4326', inplace=True)

print('Creating GeoDataFrame from population data...')
gdf_population = gpd.GeoDataFrame(df_pop,
                                  geometry=gpd.points_from_xy(df_pop.Lon, df_pop.Lat))
gdf_population.set_crs('epsg:4326', inplace=True)
print('Creating GeoDataFrame from bs data...')
gdf_bs = gpd.GeoDataFrame(df_bs,
                          geometry=gpd.points_from_xy(df_bs.lon, df_bs.lat))
gdf_bs.set_crs('epsg:4326', inplace=True)

print('Calculating # of populations per grid...')
pop_in_grid = gpd.sjoin(gdf_population, df_grid, op='within')
print('Calculating # of bs per grid...')
bs_in_grid = gpd.sjoin(gdf_bs, df_grid, op='within')

bs_in_grid.drop(['index_right'], axis=1, inplace=True)

print('Removing the BS that are out of the poly...')
bs_in_grid = gpd.sjoin(bs_in_grid, gdf_poly, op='within')
bs_in_grid = bs_in_grid[['radio', 'net', 'cell', 'lon', 'lat', 'geometry', 'id']]

bs_all_count = bs_in_grid[['id', 'geometry']].groupby('id').count().reset_index()

pop_in_grid = pop_in_grid[['id', 'geometry']]
pop_count = pop_in_grid.groupby('id').count().reset_index()

print('Population and BS alignment...')
pop_align = pd.merge(left=pop_count, right=df_grid, left_on='id', right_on='id', how='right')
bs_align = pd.merge(left=bs_all_count, right=df_grid, left_on='id', right_on='id', how='right')
pop_align.fillna(0, inplace=True)
bs_align.fillna(0, inplace=True)
pop_align.columns = ['id', 'pop', 'geometry']
bs_align.columns = ['id', 'bs', 'geometry']

pop_results = gpd.GeoDataFrame(pop_align)
pop_results.set_crs('epsg:4326', inplace=True)
pop_final = gpd.sjoin(pop_results, gdf_poly, op='within')[['id', 'pop', 'geometry']]

df_bounds = pop_final['geometry'].bounds
x = (df_bounds['minx'] + df_bounds['maxx']) / 2
y = (df_bounds['miny'] + df_bounds['maxy']) / 2
pop_final['lon'] = x.values
pop_final['lat'] = y.values
pop_final.to_file(folder + country + '/pop.geojson', driver='GeoJSON')

bs_results = gpd.GeoDataFrame(bs_align)
bs_results.set_crs('epsg:4326', inplace=True)
bs_final = gpd.sjoin(bs_results, gdf_poly, op='within')[['id', 'bs', 'geometry']]
bs_final['lat'] = x.values
bs_final['lon'] = y.values
bs_final.to_file(folder + country + '/bs.geojson', driver='GeoJSON')

pop_final['bs'] = bs_final['bs'].values
all_final = pop_final.copy()

print('Calculating imbalance index per grid...')
user_per_bs = 100
all_final['imbalance_index'] = all_final['pop'] / (all_final['bs'] * user_per_bs)
all_final.loc[(all_final['pop'] == 0) & (all_final['bs'] == 0), 'imbalance_index'] = 0.0

inf_imbalance = all_final.loc[all_final['imbalance_index'] == np.inf, 'pop'] / user_per_bs
all_final.loc[all_final['imbalance_index'] == np.inf, 'imbalance_index'] = inf_imbalance.values
all_final.to_file(folder+country+'/' + country + '_all_info.geojson', driver='GeoJSON')

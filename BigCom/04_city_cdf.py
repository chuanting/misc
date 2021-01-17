# -*- coding: utf-8 -*-
"""
-----------------------------------------------
# File: 04_city_cdf.py
# This file is created by Chuanting Zhang
# Email: chuanting.zhang@kaust.edu.sa
# Date: 2020-12-12 (YYYY-MM-DD)
-----------------------------------------------
"""
import pandas as pd
import numpy as np


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1 = np.radians(lon1), np.radians(lat1)
    lon2, lat2 = np.radians(lon2), np.radians(lat2)

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r * 3600


df_bs = pd.read_csv('D:/Dataset/cell_towers/cell_towers_2020-12-08-T000000.csv')

# df_gsm = df_bs[df_bs['radio'] == 'GSM']
# df_umts = df_bs[df_bs['radio'] == 'UMTS']
# df_cdma = df_bs[df_bs['radio'] == 'CDMA']
# df_lte = df_bs[df_bs['radio'] == 'LTE']

# # new york city
# lat_min, lat_max, lon_min, lon_max = 40.3507, 41.2083, -74.7473, -72.5022
# lat, lon = 40.730610, -73.935242

cities = [[40.3507, 41.2083, -74.7473, -72.5022, 40.730610, -73.935242],
          [32.996, 34.751, -119.561, -116.354, 34.0022, -118.1557],
          [48.165, 49.411, 1.084, 3.984, 48.8578, 2.3454],
          [39.6587, 40.1645, 115.8531, 116.9623, 39.916668, 116.383331],
          [33.0394, 34.0523, -113.0388, -110.9853, 33.448376, -112.074036],
          [-30.1608, -29.5878, 30.5969, 31.2270, -29.883333, 31.049999],
          [-29.6719, -29.5356, 30.2670, 30.5447, -29.6009, 30.3786],
          [16.9259, 17.0305, 7.9277, 8.0748, 16.9722, 7.9846],
          [-5.2804, -4.8855, 18.5383, 19.1993, -5.0456, 18.8125],
          [23.428, 25.863, 45.040, 48.582, 24.7192, 46.712],
          [0.1701, 0.4056, 32.3419, 32.7621, 0.3147, 32.5746],
          [36.3951, 37.1359, 9.4464, 10.9689, 36.7986, 10.1761],
          [34.3513, 35.2572, 9.7714, 11.6785, 34.7394, 10.7568],
          [35.048, 37.505, -117.777, -111.866, 36.1614, -115.1662],
          [37.830, 39.716, -78.287, -74.938, 38.898, -77.0358],
          [44.610, 49.268, -7.229, 4.911, 47.2162, -1.5531],
          [29.644, 31.781, 101.970, 106.313, 30.671, 104.0611],
          [2.4208, 3.1354, 31.5596, 33.1059, 2.7693, 32.3013],
          [33.705, 35.784, 67.407, 70.977, 34.5265, 69.1548],
          [30.720, 32.861, 64.094, 67.623, 31.6104, 65.7099]]

city_name = ['NYC', 'LA', 'Paris', 'Beijing', 'Phoenix', 'Durban', 'Pietermaritzburg', 'Agadez', 'Kikwit', 'Riyadh',
             'Kampala', 'Tunisia', 'Sfax', 'LasVegas', 'Washington', 'Nantes', 'Chengdu', 'Gulu', 'Kabul', 'Kandahar']

distances = []

# for idx, city_geo in enumerate(cities):
#     lat_min, lat_max, lon_min, lon_max, lat, lon = city_geo
#     df_gsm_city = df_gsm[
#         (lat_min <= df_gsm['lat']) & (df_gsm['lat'] <= lat_max) & (lon_min <= df_gsm['lon']) & (
#                     df_gsm['lon'] <= lon_max)]
#     df_umts_city = df_umts[(lat_min <= df_umts['lat']) & (df_umts['lat'] <= lat_max) & (lon_min <= df_umts['lon']) & (
#             df_umts['lon'] <= lon_max)]
#     df_lte_city = df_lte[
#         (lat_min <= df_lte['lat']) & (df_lte['lat'] <= lat_max) & (lon_min <= df_lte['lon']) & (
#                     df_lte['lon'] <= lon_max)]
#
#     dist_threshold = 100.
#
#     dist_gsm = haversine(df_gsm_city['lon'].values, df_gsm_city['lat'].values, lon, lat)
#     df_gsm_city.loc[:, 'dist'] = dist_gsm / 1000.
#     df_gsm_city = df_gsm_city[df_gsm_city['dist'] <= dist_threshold]
#     # distances.append(df_gsm_city['dist'].values)
#
#     df_gsm_city['dist'].to_csv('d:/gsm_{:}.csv'.format(idx), index=False)
#
#     dist_umts = haversine(df_umts_city['lon'].values, df_umts_city['lat'].values, lon, lat)
#     df_umts_city['dist'] = dist_umts / 1000.
#     df_umts_city = df_umts_city[df_umts_city['dist'] <= dist_threshold]
#     # distances.append(df_umts_city['dist'].values)
#     df_umts_city['dist'].to_csv('d:/umts_{:}.csv'.format(idx), index=False)
#
#     dist_lte = haversine(df_lte_city['lon'].values, df_lte_city['lat'].values, lon, lat)
#     df_lte_city['dist'] = dist_lte / 1000.
#     df_lte_city = df_lte_city[df_lte_city['dist'] <= dist_threshold]
#     df_lte_city['dist'].to_csv('d:/lte_{:}.csv'.format(idx), index=False)

for idx, city_geo in enumerate(cities):
    lat_min, lat_max, lon_min, lon_max, lat, lon = city_geo
    x = df_bs.loc[
        (lat_min <= df_bs['lat']) & (df_bs['lat'] <= lat_max) & (lon_min <= df_bs['lon']) & (
                df_bs['lon'] <= lon_max), :]
    df_city = x.copy()

    dist_threshold = 150.

    dist = haversine(df_city['lon'].values, df_city['lat'].values, lon, lat)
    df_city.loc[:, 'distance'] = (dist / 1000.)
    df_city_threshold = df_city.loc[df_city['distance'] <= dist_threshold, :]
    df_city_threshold.to_csv('d:/{:}.csv'.format(city_name[idx]), index=False)
    df_city_threshold['distance'].to_csv('d:/{:}_distance.csv'.format(city_name[idx]), index=False)


# distances.append(df_lte_city['dist'].values)

# df = pd.DataFrame(distances).T
# df.columns = ['nyc_gsm', 'nyc_umts', 'nyc_lte',
#               'beijing_gsm', 'beijing_umts', 'beijing_lte',
#               'ph_gsm', 'ph_umts', 'ph_lte',
#               'durban_gsm', 'durban_umts', 'durban_lte']
# print(df)
# df.to_csv('d:/all.csv', index=False)

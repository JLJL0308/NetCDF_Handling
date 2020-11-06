# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 12:17:03 2020

"""
from netCDF4 import Dataset
import numpy as np
import pandas as pd

# Read NetCDF
data = Dataset(r"C:\Users\Jiacheng Li\Desktop\Study\University of Birmingham Relevant\Final Year Project\NetCDF_Handling\NetCDF_data\1980.nc", "r")

# Store lon and lat data
lon = data.variables["lon"][:]
lat = data.variables["lat"][:]

# Store lon and lat value for city katmandu
lat_katmandu = 27.697871
lon_katmandu = 85.329806

# Find out the closest valid coordinates using squared value.
sq_diff_lat = (lat - lat_katmandu)**2
sq_diff_lon = (lon - lon_katmandu)**2
closest_lat_index = sq_diff_lat.argmin()
closest_lon_index = sq_diff_lon.argmin()

# Define time series
starting_date = data.variables["time"].units[14 : 24]
ending_date = data.variables["time"].units[14 : 18] + "-12-31"
data_range = pd.date_range(start = starting_date, end = ending_date)
df = pd.DataFrame(0, columns=["Average_Temparature"], index = data_range)
dt = np.arange(0, data.variables["time"].size)

# Map temparature data with time
for time_point in dt:
    df.iloc[time_point] = data.variables["tave"][time_point, closest_lat_index, closest_lon_index]
    
# Export as CSV file
df.to_csv("Temparature_Katmandu.csv")

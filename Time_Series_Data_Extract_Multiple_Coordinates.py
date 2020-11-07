# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 06:54:43 2020

"""
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import os

# Read NetCDF
data = Dataset(r"C:\Users\Jiacheng Li\Desktop\Study\University of Birmingham Relevant\Final Year Project\NetCDF_Handling\NetCDF_data\1980.nc", "r")

# Store lon and lat data
lon = data.variables["lon"][:]
lat = data.variables["lat"][:]

# Define time series
starting_date = data.variables["time"].units[14 : 24]
ending_date = data.variables["time"].units[14 : 18] + "-12-31"
data_range = pd.date_range(start = starting_date, end = ending_date)
df = pd.DataFrame(0, columns=["Average_Temparature"], index = data_range)
dt = np.arange(0, data.variables["time"].size)

# Map temparature data with time in multiple coordinates.
os.chdir(r"C:\Users\Jiacheng Li\Desktop\Study\University of Birmingham Relevant\Final Year Project\NetCDF_Handling\Time_Series_Multiple_Coordinates")
for lat_iterater in np.arange(start = 0, stop = len(lat), step = 10):
    for lon_iterater in np.arange(start = 0, stop = len(lon), step = 10):
        for time_point in dt:
            df.iloc[time_point] = data.variables["tave"][time_point, lat[lat_iterater], lon[lon_iterater]]
        # Export as CSV file
        df.to_csv(str(lat[lat_iterater]) + "&" + str(lon[lon_iterater]) + ".csv")
        
    

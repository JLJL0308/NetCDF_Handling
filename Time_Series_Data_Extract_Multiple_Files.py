# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 06:28:59 2020

"""
import glob
import os
from netCDF4 import Dataset
import pandas as pd
import numpy as np

all_years = []

# Change to the directory where the data is stored.
os.chdir(r"C:\Users\Jiacheng Li\Desktop\Study\University of Birmingham Relevant\Final Year Project\NetCDF_Handling\NetCDF_data")

# Store the file names into a list.
for file in glob.glob("*.nc"):
    print(file)
    data = Dataset(file, "r")
    time = data.variables["time"]
    year = time.units[14 : 18]
    all_years.append(year)
    
# Create a pandas DatetimeIndex to store all dates.
year_start = min(all_years)
year_end = max(all_years)
date_range = pd.date_range(start = year_start + "-01-01",
                           end = year_end + "-12-31",
                           freq = "D")
# Create an empty pandas dataframe with date as the index.
df = pd.DataFrame(0.0, columns = ["Temparature"], index = date_range)

# Varibles to store the coordinates for city Katmandu
lat_katmandu = 27.697817
lon_katmandu = 85.329806

# Sort the list just in case they don't appear in order in the directory.
all_years.sort()

# Loop through all files and extract the lat, lon, and temp data.
for year in all_years:
    data = Dataset(year + ".nc", "r")
    lat = data.variables["lat"][:]
    lon = data.variables["lon"][:]
    sq_diff_lat = (lat - lat_katmandu)**2
    sq_diff_lon = (lon - lon_katmandu)**2
    min_index_lat = sq_diff_lat.argmin()
    min_index_lon = sq_diff_lon.argmin()
    temp = data.variables["tave"]
    start = year + "-01-01"
    end = year + "-12-31"
    year_date_range = pd.date_range(start = start,
                                    end = end,
                                    freq = "D")
    # Nested loop to extract daily data from the file.
    for t_index in np.arange(0, len(year_date_range)):
        df.loc[year_date_range[t_index]]["Temparature"] = temp[t_index, min_index_lat, min_index_lon]
        
df.plot()

# Change to the directory where the data needs to be stored.
os.chdir(r"C:\Users\Jiacheng Li\Desktop\Study\University of Birmingham Relevant\Final Year Project\NetCDF_Handling")
# Save the data.
df.to_csv("Temparature in Katmandu from 1980 to 1981.csv")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
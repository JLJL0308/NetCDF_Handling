# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 08:56:11 2020

"""
from netCDF4 import Dataset
import numpy as np

# Read NetCDF
data = Dataset(r"C:\Users\Jiacheng Li\Desktop\Study\University of Birmingham Relevant\Final Year Project\NetCDF_Handling\NetCDF_data\1980.nc", "r")

#print(data)
#print(type(data))
#print(data.variables.keys())

# Check varibles
# lon = data.variables["lon"]
# print(lon,"\n")
# 
# lat = data.variables["lat"]
# print(lat,"\n")
# 
# time = data.variables["time"]
# print(time,"\n")
# 
# tave = data.variables["tave"]
# print(tave,"\n")
# 
# rstn = data.variables["rstn"]
# print(rstn,"\n")

# Access data
time_data = data.variables["time"][:]
print(time_data)

lon_data = data.variables["lon"][:]
print(lon_data)

lat_data = data.variables["lat"][:]
print(lat_data)

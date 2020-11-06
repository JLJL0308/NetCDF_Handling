# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 14:07:32 2020

"""
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

data = Dataset(r"C:\Users\Jiacheng Li\Desktop\Study\University of Birmingham Relevant\Final Year Project\NetCDF_Handling\NetCDF_data\1980.nc", "r")

lats = data.variables["lat"][:]
lons = data.variables["lon"][:]
time = data.variables["time"][:]
tave = data.variables["tave"][:]

mp = Basemap(projection = "merc",
             llcrnrlon = 65.8, 
             llcrnrlat = -2, 
             urcrnrlon = 145.37, 
             urcrnrlat = 38.78, 
             resolution = "i")

lon, lat = np.meshgrid(lons, lats)
x, y = mp(lon, lat)

colorMap = mp.pcolor(x, y, np.squeeze(tave[0,:,:]), cmap = "rainbow")
mp.drawcoastlines()
mp.drawstates()
mp.drawcountries()

char = mp.colorbar(colorMap, location = "right", pad = "10%")

plt.title("Average Temparature on 01-01-1980")
plt.show()

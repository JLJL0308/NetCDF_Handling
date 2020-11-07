# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 20:47:43 2020

"""
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

data = Dataset(r"C:\Users\Jiacheng Li\Desktop\Study\University of Birmingham Relevant\Final Year Project\NetCDF_Handling\NetCDF_data\1980.nc", "r")

# Store different variables.
lats = data.variables["lat"][:]
lons = data.variables["lon"][:]
time = data.variables["time"][:]
tave = data.variables["tave"][:]

# Create a basemap in a specified region using coordinates.
mp = Basemap(projection = "merc",
             llcrnrlon = 65.8, 
             llcrnrlat = -2, 
             urcrnrlon = 145.37, 
             urcrnrlat = 38.78, 
             resolution = "i")

lon, lat = np.meshgrid(lons, lats)
x, y = mp(lon, lat)
days = np.arange(0, len(time))

# Generate images in jpg format.
for day in days:
    colorMap = mp.pcolor(x, y, np.squeeze(tave[day,:,:]), cmap = "rainbow")
    mp.drawcoastlines()
    mp.drawstates()
    mp.drawcountries()
    char = mp.colorbar(colorMap, location = "right", pad = "10%")
    plt.title("Average Temparature Day:" + str(day + 1) + "of Year 1980")
    plt.clim(-40, 40)
    plt.savefig("Images/" + str(day + 1) + ".jpg")
    # Clear the plot at the end of each loop.
    plt.clf()

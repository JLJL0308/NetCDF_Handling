# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 05:51:43 2020

"""
import PIL
import numpy as np

frames = []
days = np.arange(1, 367)

# Store images in a frame.
for day in days:
    tempFrame = PIL.Image.open("Images/" + str(day) + ".jpg")
    frames.append(tempFrame)

# Save the frame as a GIF.
frames[0].save("Temparature_Timelapse.gif", format = "GIF",
               append_images = frames[1 : ],
               save_all = True,
               duration = 200,
               loop = 0)

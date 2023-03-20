#Code to generate a graphic for the map of Europe with grid lines
#You need those packages
import os

import cartopy.crs as ccrs
import cartopy.feature as cf

import matplotlib.pyplot as plt

from matplotlib.image import imread

from PIL import Image

#allows for the image to load despite a large number of pixels
Image.MAX_IMAGE_PIXELS = 1000000000 

#figure size and type of map projection used, for the best result the same map projection should be used for both a source image and the final map
plt.figure(figsize=(20, 15), dpi=150)
ax = plt.axes(projection=ccrs.PlateCarree())

#image map projection, depends on the image file
source_proj = ccrs.PlateCarree()

#loads map image from the path (map comes from Natural Earth Data)
fname = os.path.join('C:/Users/macie/OneDrive/Desktop/Project_A02/Map_projection', 'NE2_HR_LC_SR_W_DR.tif')
ax.imshow(imread(fname), origin='upper', transform=source_proj, extent=[-180, 180, -90, 90])

#generates 2.8 x 2.8 degree grid onto the map
xlines = []
ylines = []
for i in range(-100, 100):
    xlines.append(i*2.8125)
for i in range(-100, 100):
    ylines.append(i*2.8125)
ax.gridlines(xlocs=xlines, ylocs=ylines, linewidth = 0.5 , color = 'black')

#adds country borders
ax.add_feature(cf.BORDERS)

#size of the showcased map (longitude, latitude)
extent = [-10, 50, 30, 70]
ax.set_extent(extent)
ax.coastlines(resolution='10m')

plt.show()
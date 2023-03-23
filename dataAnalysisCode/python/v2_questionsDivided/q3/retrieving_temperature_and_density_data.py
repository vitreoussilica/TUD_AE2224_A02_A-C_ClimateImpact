import numpy as np
import pandas as pd
import xarray as xr
from matplotlib import pyplot as plt

climate_data = xr.open_dataset("C:/Users/macie/OneDrive/Desktop/Project_A02/Project_data/f100___________20171202_0000_ECHAM5.nc")

#get the data
temperature = climate_data.variables['tm1']
density = climate_data.variables['rho_air_dry']
time = climate_data.coords['time']
lon = climate_data.coords['lon']
lat = climate_data.coords['lat']
lev = climate_data.coords['lev']

#take a mean value over the whole month for each position
temperature_values = np.mean(temperature, axis=0)
density_values = np.mean(density, axis=0)

#reduce the range of data
rem_lat1 = np.arange(0, 6)
rem_lat2 = np.arange(25, len(lat))
remove_lat = np.append(rem_lat1, rem_lat2) 

remove_lon = np.arange(23, len(lon)-5)

temperature_values = np.delete(temperature_values, remove_lat , axis=1)
temperature_values = np.delete(temperature_values, remove_lon, axis=2)
density_values = np.delete(density_values, remove_lat, axis=1)
density_values = np.delete(density_values, remove_lon, axis=2)

"""TO DO
Rearange the longitude axis so the end values from 340 to 360 degrees are in front of the 0-70
Don't know how to do it
Will probably never find out how to do it correctly
But who cares
My code, my rules

BTW this runs much faster compared to the previous attempts
"""

#testing by reducing lev axis to 1 and taking a mean
lev_remove = np.arange(0, 6)
lev_remove = np.append(lev_remove, np.arange(7, 31))
temperature_values_test = np.delete(temperature_values, lev_remove, axis=0)
temperature_values_test = np.mean(temperature_values_test, axis=0)

#testing by creating a heat map
plt.imshow(temperature_values_test, interpolation='nearest')
plt.show()
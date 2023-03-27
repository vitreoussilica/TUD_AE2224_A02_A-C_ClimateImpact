import numpy as np
import pandas as pd
import xarray as xr
from matplotlib import pyplot as plt

M = 0.8
FT = 0
gamma = 1.4
R = 287.05

climate_data = xr.open_dataset("C:/Users/macie/OneDrive/Desktop/Project_A02/Project_data/f100___________20171202_0000_ECHAM5.nc")

#get the data
temperature = climate_data.variables['tm1']
density = climate_data.variables['rho_air_dry']
time = climate_data.coords['time']
lon = climate_data.coords['lon']
lat = climate_data.coords['lat']
lev = climate_data.coords['lev']

#take a mean value over the whole month for each position
temperature_values = xr.DataArray.mean(temperature, axis=0)
density_values = xr.DataArray.mean(density, axis=0)

"""TO DO
Rearange the longitude axis so the end values from 340 to 360 degrees are in front of the 0-70
Don't know how to do it
Will probably never find out how to do it correctly
But who cares
My code, my rules

BTW this runs much faster compared to the previous attempts
"""

velocity = M * np.sqrt(temperature_values.data*gamma*R)
print(velocity)
#temperature_values_test = xr.DataArray.mean(temperature_values, axis=0)


#testing by creating a heat map
# plt.imshow(temperature_values_test, interpolation='nearest')
# plt.savefig("test_xr")
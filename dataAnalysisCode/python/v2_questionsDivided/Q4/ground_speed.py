import numpy as np
import xarray as x
import matplotlib.pyplot as plt
'''
Altitude, Ground Speed, ATR20
    - Altitude
    - Ground speed
    - Cumulative ATR -- done by Q2
'''

data_airtraf = x.open_dataset("/Users/annika/Desktop/Project/Full_Data/DT00/f100___________20171202_0000_airtraf_ac.nc", engine='netcdf4')

print('Airtraf data variables:')
data = data_airtraf.variables['routes_out'].data
# Data altitude & ground speed
altitude = data[0,0,2,:]
ground_speed = data[0,0,4,:]

# Splitting data into 3 different heights
#8500-9500
i = np.where(altitude<9500.)[0]
altitude_8500 = altitude[i]
ground_8500 = ground_speed[i]
#9500-10500
i = np.where(altitude>9500.)[0]
j = np.where(altitude<10500.)[0]
k = np.array([x for x in i if x in j])
altitude_9500 = altitude[k]
ground_9500 = ground_speed[k]
#10500-11500
i = np.where(altitude>10500.)[0]
altitude_10500 = altitude[i]
ground_10500 = ground_speed[i]

plt.figure(figsize=(8, 6))
plt.scatter(altitude_8500, ground_8500, color="red", marker=".", label="8500-9500")
plt.scatter(altitude_9500, ground_9500, color="green", marker=".", label="9500-10500")
plt.scatter(altitude_10500, ground_10500, color="blue", marker=".", label="10500-11500")
plt.xlabel("Altitude [m]")
plt.ylabel("Ground speed [km/h]")
plt.legend()
plt.show()

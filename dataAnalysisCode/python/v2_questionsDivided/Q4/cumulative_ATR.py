import numpy as np
import xarray as x
import matplotlib.pyplot as plt
import filenames as fn

'''
Altitude & ATR20
    - Altitude
    - Cumulative ATR
'''

filenames = fn.all_filenames_airtraf_ac_DT00('/Users/annika/Desktop/Project/Full_Data')

altitude = np.zeros((1))
cumulative_ATR = np.zeros((1))
for filename in filenames:
    dataset = x.open_dataset(filename)
    data = dataset.variables['routes_out'].data
    # Data altitude & cumulative ATR
    altitude = np.concatenate((altitude, data[0,0,2,:]))
    cumulative_ATR = np.concatenate((cumulative_ATR, data[0,0,15,:]))

# To get rid of values created by np.zeros in lines 15-16 earlier
altitude = np.delete(altitude, 0)
cumulative_ATR = np.delete(cumulative_ATR, 0)

# Splitting data into 3 different heights
#8500-9500
i = np.where(altitude<9500.)[0]
altitude_8500 = altitude[i]
ATR_8500 = cumulative_ATR[i]
#9500-10500
i = np.where(altitude>9500.)[0]
j = np.where(altitude<10500.)[0]
k = np.array([x for x in i if x in j])
altitude_9500 = altitude[k]
ATR_9500 = cumulative_ATR[k]
#10500-11500
i = np.where(altitude>10500.)[0]
altitude_10500 = altitude[i]
ATR_10500 = cumulative_ATR[i]

plt.figure(figsize=(8, 6))
plt.scatter(altitude_8500, ATR_8500, color="red", marker=".", label="8500-9500")
plt.scatter(altitude_9500, ATR_9500, color="green", marker=".", label="9500-10500")
plt.scatter(altitude_10500, ATR_10500, color="blue", marker=".", label="10500-11500")
plt.xlabel("Altitude [m]")
plt.ylabel("ATR20 [K]")
plt.legend()
plt.show()

import sys
sys.path.insert(1, '/Users/annika/Desktop/Project/TUD_AE2224_A02_A-C_ClimateImpact-Q2_Gerben/dataAnalysisCode/python/v2_questionsDivided/Q2')
import numpy as np
import xarray as x
import matplotlib.pyplot as plt
import ATR_per_emission as atr
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
cumulative_ATR = data[0,0,15,:]

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

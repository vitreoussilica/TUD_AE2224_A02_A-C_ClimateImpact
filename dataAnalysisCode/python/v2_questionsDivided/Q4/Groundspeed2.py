import numpy as np
import xarray as x
import matplotlib.pyplot as plt
import filenames as fn
'''
Altitude, Ground Speed, ATR20
    - Altitude
    - Ground speed
    - Cumulative ATR -- done by Q2
'''

#for i in range(14):
#    filepaths = fn.all_filenames_for_month("/Users/milan/OneDrive - Delft University of Technology/Project_Y2Q3-4/AT20_optimal", 'airtraf_ac.nc', i)
#print(filepaths)



filenames = fn.all_filenames_airtraf_ac_DT00('C:/Users/milan/OneDrive - Delft University of Technology/Project_Y2Q3-4/AT20_optimal')
print(filenames)

altitude = np.zeros((1))
ground_speed = np.zeros((1))

for filename in filenames:
    dataset = x.open_dataset(filename)
    data = dataset.variables['routes_out'].data

    altitude = np.concatenate((altitude, data[0,0,2,:]))
    ground_speed = np.concatenate((ground_speed, data[0,0,4,:]))

np.delete(altitude, 0)
np.delete(ground_speed, 0)




# Data altitude & ground speed

#altitude = np.concatenate((data1[0,0,2,:], data2[0,0,2,:], data3[0,0,2,:]))
#ground_speed = np.concatenate((data1[0,0,4,:], data2[0,0,4,:], data3[0,0,4,:]))


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
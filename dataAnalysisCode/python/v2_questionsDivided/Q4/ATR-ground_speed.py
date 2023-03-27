import numpy as np
import xarray as x
import matplotlib.pyplot as plt
import filenames as fn
'''
ground_speed, Ground Speed, ATR20
    - ground_speed
    - Ground speed
    - Cumulative ATR -- done by Q2
'''

filenames = fn.all_filenames_airtraf_ac_DT00('C:/Users/milan/OneDrive - Delft University of Technology/Project_Y2Q3-4/AT20_optimal')
print(filenames)

ground_speed = np.zeros((1))
cumulative_ATR = np.zeros((1))
print(ground_speed)
for filename in filenames:
    dataset = x.open_dataset(filename)
    data = dataset.variables['routes_out'].data

    ground_speed = np.concatenate((ground_speed, data[0,0,4,:]))
    cumulative_ATR = np.concatenate((cumulative_ATR, data[0,0,15,:]))

ground_speed = np.delete(ground_speed, 0)
cumulative_ATR = np.delete(cumulative_ATR, 0)



print('Airtraf data variables:')

# Splitting data into 3 different heights
#8500-9500
i = np.where(ground_speed<800.)[0]
ground_speed_800 = ground_speed[i]
ATR_8500 = cumulative_ATR[i]
#9500-10500
i = np.where(ground_speed>800.)[0]
j = np.where(ground_speed<900.)[0]
k = np.array([x for x in i if x in j])
ground_speed_900 = ground_speed[k]
ATR_9500 = cumulative_ATR[k]
#10500-11500
i = np.where(ground_speed>900.)[0]
ground_speed_1000 = ground_speed[i]
ATR_10500 = cumulative_ATR[i]

plt.figure(figsize=(8, 6))
plt.scatter(ground_speed_800, ATR_8500, color="red", marker=".", label="8500-9500")
plt.scatter(ground_speed_900, ATR_9500, color="green", marker=".", label="9500-10500")
plt.scatter(ground_speed_1000, ATR_10500, color="blue", marker=".", label="10500-11500")
plt.xlabel("ground_speed [km/h]")
plt.ylabel("ATR20 [K]")
plt.legend()
plt.show()
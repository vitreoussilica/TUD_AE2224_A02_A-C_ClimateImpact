import xarray as x
import matplotlib.pyplot as plt

'''
Useful variables ECHAM:
    - Large-scale/convective rain/snow (rate) -- combine large-scale and convective for the total rate
    - u-winds/v-winds -- in dir. of grid
    - Specific/**relative** humidity/temperature -- relative is the more relevant one; since it has to do with the total humidity too
    - Cloud water/ice
    - Vertical wind velocity -- vertical from Earth
'''

data_airtraf = x.open_dataset("/Users/annika/Desktop/Project/Full_Data/DT00/f100___________20171202_0000_airtraf_ac.nc", engine='netcdf4')
data_ECHAM = x.open_dataset("/Users/annika/Desktop/Project/Full_Data/DT00/f100___________20171202_0000_ECHAM5.nc", engine='netcdf4')

print('ECHAM data variables:')
data = data_ECHAM.variables
print(data)

# Data altitude & weather conditions
altitude = ...
rainr = data['rsfl_2d'].data + data['rsfc_2d'].data  # Large-scale + convective rain rate
snowr = data['ssfl_2d'].data + data['ssfc_2d'].data  # Large-scale + convective snow rate
u_wind = data['um1'].data
v_wind = data['vm1'].data
rel_hum = data['rhum'].data
cloud_water = data['xlm1'].data
cloud_ice = data['xim1'].data
vert_wind = data['etadot'].data

plt.figure(figsize=(8, 6))
plt.scatter(altitude, rainr, color="red", marker=".", label="Rain rate")
plt.scatter(altitude, snowr, color="green", marker=".", label="Snow rate")
plt.xlabel("Altitude [m]")
plt.ylabel("Rain/snow rate [kg/m^2/s]")
plt.legend()
plt.show()
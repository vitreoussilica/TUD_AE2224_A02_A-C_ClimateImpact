import numpy as np
import matplotlib.pyplot as plt

# Import the relative ATR values of individual emissions for two routes: 
# minimal climate impact and optimal climate impact with 1 percent increase in operating costs
#co2
carbondiox_minclim = [0, -0.24, -0.57]
averageco_minclim = sum(carbondiox_minclim) / len(carbondiox_minclim)
carbondiox_1perc = [0, -0.24, -0.57]
averageco_1perc = sum(carbondiox_1perc) / len(carbondiox_1perc)
cox= [0, averageco_minclim, averageco_1perc]
#nox
nitoxides_minclim  = [0, -0.13, -0.30]
averagenitoxides_minclim = sum(nitoxides_minclim) / len(nitoxides_minclim)
nitoxides_1perc  = [0, -0.07, -0.1]
averagenitoxides_1perc= sum(nitoxides_1perc) / len(nitoxides_1perc)
nox= [0, averagenitoxides_minclim, averagenitoxides_1perc]
#waterw
waterw_minclim  =  [0, -0.07, -0.1]
averagewaterw_minclim =sum(waterw_minclim) / len(waterw_minclim)
waterw_1perc  = [0, -0.07, -0.1]
averagewaterw_1perc = sum(waterw_1perc) / len(waterw_1perc)
ww= [0, averagewaterw_minclim, averagewaterw_1perc]
#contrails
contrails_minclim = [0, -0.3, -0.75]
averagecontrails_minclim = sum(contrails_minclim) / len(contrails_minclim)
contrails_1perc  = [0, -0.07, -0.1]
averagecontrails_1perc= sum(contrails_1perc) / len(contrails_1perc)
contrails= [0, averagecontrails_minclim , averagecontrails_1perc]

# Import fuel consumption data
fuel_data_1perc = 0.1
#cox
fuel_data_minclim_co = [0, 0.3, 0.75]
average_minclim_co= sum(fuel_data_minclim_co) / len(fuel_data_minclim_co)
fuel_data_co= [0, fuel_data_1perc, average_minclim_co]
#nox
fuel_data_minclim_no = [0, 0.3, 0.75]
average_minclim_no= sum(fuel_data_minclim_no) / len(fuel_data_minclim_no)
fuel_data_no= [0, fuel_data_1perc, average_minclim_no]
#ww
fuel_data_minclim_ww = [0, 0.3, 0.75]
average_minclim_ww= sum(fuel_data_minclim_ww) / len(fuel_data_minclim_ww)
fuel_data_ww= [0, fuel_data_1perc, average_minclim_ww]
#con
fuel_data_minclim_con = [0, 0.3, 0.75]
average_minclim_con= sum(fuel_data_minclim_con) / len(fuel_data_minclim_con)
fuel_data_con= [0, fuel_data_1perc, average_minclim_con]

# Interpolate the data points with a polynomial
x_carbondiox = np.linspace(min(cox), max(cox), 100)
f_carbondiox = np.poly1d(np.polyfit(cox, fuel_data_co, 15))
y_carbondiox = f_carbondiox(x_carbondiox)

x_nitoxides = np.linspace(min(nox), max(nox), 100)
f_nitoxides = np.poly1d(np.polyfit(nox, fuel_data_no, 15))
y_nitoxides = f_nitoxides(x_nitoxides)

x_waterw = np.linspace(min(ww), max(ww), 100)
f_waterw = np.poly1d(np.polyfit(ww, fuel_data_ww, 15))
y_waterw = f_waterw(x_waterw)

x_contrails = np.linspace(min(contrails), max(contrails), 100)
f_contrails = np.poly1d(np.polyfit(contrails, fuel_data_con, 15))
y_contrails = f_contrails(x_contrails)

# Plot the scatter plot and interpolated curves
plt.figure(figsize=(8, 6))
#co2
plt.scatter(averageco_minclim, average_minclim_co, color='purple', label='Carbondioxide')
plt.scatter(averageco_1perc, fuel_data_1perc, color='purple')
#nox
plt.scatter(averagenitoxides_minclim, average_minclim_no, color='green', label='Nitrogen Oxides')
plt.scatter(averagenitoxides_1perc, fuel_data_1perc, color='green')
#waterwapor
plt.scatter(averagewaterw_minclim, average_minclim_ww, color='orange', label='Water Wapor')
plt.scatter(averagewaterw_1perc, fuel_data_1perc, color='orange')
#contrails
plt.scatter(averagecontrails_minclim, average_minclim_con, color='blue', label='Contrails')
plt.scatter(averagecontrails_1perc, fuel_data_1perc, color='blue')

#plt.plot(x_carbondiox, y_carbondiox, color='purple', label='Carbondioxide Parabola')
#plt.plot(x_nitoxides, y_nitoxides, color='green', label='Nitrogen Oxides Parabola')
#plt.plot(x_waterw, y_waterw, color='orange', label='Water wapor Parabola')
#plt.plot(x_contrails, y_contrails, color='blue', label='Contrails Parabola')

plt.xlabel(r'Relative Average Temperature Response ($\Delta$$ATR_{rel}$)')
plt.ylabel(r'Relative Fuel Consumption ($\Delta$$Fuel_{rel}$)')
plt.title('Pareto Fronts of emissions for optimized trajectories')
plt.legend(loc='lower left')
plt.grid(b = True, color ='grey', linestyle ='-.', linewidth = 0.5, alpha = 0.6)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("/Users/annika/Desktop/Project/TUD_AE2224_A02_A-C_ClimateImpact-main/dataAnalysisCode/python/v2_questionsDivided/Q4/aa_high_potential_list_unsorted.txt", delimiter=',')

data = data[(data[:,2]==1)]  # Keep only noon values
data[:,1] = data[:,1] + 1    # Make days start at 1 and not 0

days = np.unique(data[:,:2], axis=0)  # Makes a list containing each unique day in the data

atr_dict = {}  # Using a dictionary for convenience in fetching values
               # Example use: atr_dict["13/12"] will give you the total ATR for the 13th of December

for day in days:
    day_data = data[np.logical_and(data[:,0]==day[0], data[:,1]==day[1]), :]  # Selects the portion of the data for a specific day
    day_atr = sum(day_data[:, 7])                                             # Adds up all ATR's for that day
    atr_dict["{1}/{0}".format(int(day[0]), int(day[1]))] = day_atr            # Creates an entry in atr_dict for that day

sorted_atr_dict = dict(sorted(atr_dict.items(), key = lambda x: x[1], reverse = False))

print(sorted_atr_dict)

# Plot
x = np.arange(365)
y = -1 * np.array(list(atr_dict.values()))  # List of all ATR's, ordered chronologically 
plt.plot(x, y, color='b')
plt.show()

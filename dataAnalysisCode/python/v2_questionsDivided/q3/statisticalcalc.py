import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
np.random.seed(1)
date2 = pd.array(pd.date_range(start ='1-1-2018', end ='12-31-2018', freq ='D'))
daynight = np.random.rand(365)
for i in range(len(daynight)):
    if daynight[i] <= 0.5:
        daynight[i] = 1
    else:
        daynight[i] = 0
daynight2 = pd.array(daynight)
corrclass = np.random.normal(50,23.5,365)
for i in range(len(corrclass)):
    if corrclass[i] <= 0:
        corrclass[i] = 0
    elif corrclass[i] >= 100:
        corrclass[i] = 100
    corrclass[i] = round(corrclass[i])
corrclass2 = pd.array(corrclass)
sampledata2 = pd.DataFrame({'date':date2, 'daynight':daynight2,'corrclass':corrclass2})

def plotfunction(sampledata,date,daynight,corrclass,monthnumber):
    corrclass2 = sampledata.corrclass


    plt.hist(corrclass2, bins = 101)
    plt.show()

    nbin, pbin = 100, 0.5
    x = np.arange(binom.ppf(0.01, nbin, pbin),
                  binom.ppf(0.99, nbin, pbin))

    onetohundred = list(range(0,101))

    corrclassamount = np.zeros(101)
    for i in range(len(corrclassamount)):
        for j in range(len(corrclass2)):
            if corrclass[j] == i:
                corrclassamount[i] += 1


    plt.vlines(onetohundred, 0, corrclassamount/365, colors = 'b', lw = 4 )
    plt.plot(x, binom.pmf(x, nbin, pbin), 'ro', ms=4, label='binom pmf')
    plt.show()

    #day
    daytime = np.zeros(101)
    nighttime = np.zeros(101)
    amountdaytime = 0
    amountnighttime = 0
    for i in range(len(daytime)):
        for j in range(len(sampledata.daynight)):
            if sampledata.corrclass[j] == i:
                if sampledata.daynight[j] == 1:
                    daytime[i] += 1
                    amountdaytime += 1
                else:
                    nighttime[i] +=1
                    amountnighttime +=1


    plt.vlines(onetohundred, 0, daytime/amountdaytime, colors = 'b', lw = 4 )
    plt.plot(x, binom.pmf(x, nbin, pbin), 'ro', ms=4, label='binom pmf')
    plt.show()

    plt.vlines(onetohundred, 0, nighttime/amountnighttime, colors = 'b', lw = 4 )
    plt.plot(x, binom.pmf(x, nbin, pbin), 'ro', ms=4, label='binom pmf')
    plt.show()

    montharray = np.zeros(101)
    monthamount = 0
    for i in range(len(montharray)):
        for j in range(len(sampledata.date)):
            if pandas.Timestamp(sampledata.date[j]).month == monthnumber:
                if sampledata.corrclass[j] == i:
                    montharray[i] += 1
                    monthamount += 1
    plt.vlines(onetohundred, 0, montharray/ monthamount, colors='b', lw=4)
    plt.plot(x, binom.pmf(x, nbin, pbin), 'ro', ms=4, label='binom pmf')
    plt.show()


plotfunction(sampledata2,date2,daynight2,corrclass2,2)


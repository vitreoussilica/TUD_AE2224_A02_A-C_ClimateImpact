import sys
sys.path.insert(1, '/Users/gerbendrijfhout/Desktop/Project/TUD_AE2224_A02_A-C_ClimateImpact/dataAnalysisCode/python/v1')

import flight as f
import retrieve_flight_data_general as fdg
import filenames as fn
import export_routes as er

import xarray as x

##all_files = fn.all_filenames_airtraf_ac("/Users/gerbendrijfhout/Desktop/Project/Full_data")
##all_flights = fdg.files_to_flight_objects(all_files)
routes_list = er.all_route_coordinates()

def total(flight: f.Flight, field: int):
    ATR_sum = 0.0
    for i in range(0, flight.data.shape[1]):
        ATR_sum += flight.data[field, i]

    print(ATR_sum)
    return ATR_sum

def is_full_set(flight_triplet: list):    
    ## Then check that the optimisation of each flight is different
    ## And check that all other fields are the same
    for i in range(0,3):
        for j in range(0,3):
            if i != j:
                if flight_triplet[i].optimisation == flight_triplet[j].optimisation:
                    return False
                if flight_triplet[i].datestamp != flight_triplet[j].datestamp:
                    return False
                if flight_triplet[i].day != flight_triplet[j].day:
                    return False
                if flight_triplet[i].time != flight_triplet[j].time:
                    return False
                if flight_triplet[i].route != flight_triplet[j].route:
                    return False
    return True
triplets = []
for i in range(0,13):
    filepaths = fn.all_filenames_for_month("/Users/gerbendrijfhout/Desktop/Project/Full_data", 'airtraf_ac.nc', i)
    flights_in_month = fdg.files_to_flight_objects(filepaths)

    for j in range(0, 32):
        flights_on_day = []
        for flight in flights_in_month:
            if flight.day == j:
                flights_on_day.append(flight)

        for k in range(0, 2):
            flights_at_time = []
            for flight in flights_on_day:
                if flight.time == k:
                    flights_at_time.append(flight)

            for l in range(0,100):
                flight_trio = []
                for flight in flights_at_time:
                    if flight.route == routes_list[l]:
                        flight_trio.append(flight)
                if len(flight_trio) == 3:
                    flight_trio.sort(key=lambda x: x.optimisation)
                    triplets.append((flight_trio[0], flight_trio[1], flight_trio[2]))
                    continue


deltas_ATR_NOX_Ozone_compromise = []
deltas_ATR_NOX_Ozone_max = []

deltas_ATR_NOX_Methane_compromise = []
deltas_ATR_NOX_Methane_max = []

deltas_ATR_Water_Vapour_compromise = []
deltas_ATR_Water_Vapour_max = []

deltas_ATR_Contrails_compromise = []
deltas_ATR_Contrails_max = []

deltas_ATR_CO2_compromise = []
deltas_ATR_CO2_max = []

deltas_ATR_Total_compromise = []
deltas_ATR_Total_max = []

negative_triplets = []

def delta_ATR_x(totals: list):
    if totals[0] > 0 and totals[1] > 0:
        delta_ATR_x_compromise =  -1 *  (1 - totals[1] / totals[0])
        delta_ATR_x_max = -1 * (1 - totals[2] / totals[0]) 
    elif totals[0] > 0 and totals[1] < 0:
        delta_ATR_x_compromise = -1 + totals[1] / totals[0]
        delta_ATR_x_max = -1 + totals[0] / totals[0]
    elif totals[0] > 0 and totals[2] < 0:
        delta_ATR_x_compromise = -1 *  (1 - totals[1] / totals[0])
        delta_ATR_x_max = -1 + totals[1] / totals[0]
    elif totals[0] < 0 and totals[1] < 0  and totals[2] < 0:
        delta_ATR_x_compromise = 0
        delta_ATR_x_max = 0
    else:
        delta_ATR_x_compromise = 0
        delta_ATR_x_max = 0

    return delta_ATR_x_compromise, delta_ATR_x_max

for triplet in triplets:
    #ATRs = [triplet[0].total_ATR(), triplet[1].total_ATR(), triplet[2].total_ATR()]
    totals_NOX_Ozone = [triplet[0].total_ATR_NOX_Ozone(), triplet[1].total_ATR_NOX_Ozone(), triplet[2].total_ATR_NOX_Ozone()]
    totals_NOX_Methane = [triplet[0].total_ATR_NOX_Methane(), triplet[1].total_ATR_NOX_Methane(), triplet[2].total_ATR_NOX_Methane()]
    totals_Water_Vapour = [triplet[0].total_ATR_Water_Vapour(), triplet[1].total_ATR_Water_Vapour(), triplet[2].total_ATR_Water_Vapour()]
    totals_Contrails = [triplet[0].total_ATR_Contrails(), triplet[1].total_ATR_Contrails(), triplet[2].total_ATR_Contrails()]
    totals_CO2 = [triplet[0].total_ATR_CO2(), triplet[1].total_ATR_CO2(), triplet[2].total_ATR_CO2()]
    totals_Total = [triplet[0].total_ATR(), triplet[1].total_ATR(), triplet[2].total_ATR()]

    deltas_ATR_NOX_Ozone_compromise.append(delta_ATR_x(totals_NOX_Ozone)[0])
    deltas_ATR_NOX_Ozone_max.append(delta_ATR_x(totals_NOX_Ozone)[1])

    deltas_ATR_NOX_Methane_compromise.append(delta_ATR_x(totals_NOX_Methane)[0])
    deltas_ATR_NOX_Methane_max.append(delta_ATR_x(totals_NOX_Methane)[1])

    deltas_ATR_Water_Vapour_compromise.append(delta_ATR_x(totals_Water_Vapour)[0])
    deltas_ATR_Water_Vapour_max.append(delta_ATR_x(totals_Water_Vapour)[1])

    deltas_ATR_Contrails_compromise.append(delta_ATR_x(totals_Contrails)[0])
    deltas_ATR_Contrails_max.append(delta_ATR_x(totals_Contrails)[1])

    deltas_ATR_CO2_compromise.append(delta_ATR_x(totals_CO2)[0])
    deltas_ATR_CO2_max.append(delta_ATR_x(totals_CO2)[1])

    deltas_ATR_Total_compromise.append(delta_ATR_x(totals_Total)[0])
    deltas_ATR_Total_max.append(delta_ATR_x(totals_Total)[1])

print(deltas_ATR_NOX_Ozone_compromise)
print(deltas_ATR_NOX_Ozone_max)

print(deltas_ATR_NOX_Methane_compromise)
print(deltas_ATR_NOX_Methane_max)

print(deltas_ATR_Water_Vapour_compromise)
print(deltas_ATR_Water_Vapour_max)

print(deltas_ATR_Contrails_compromise)
print(deltas_ATR_Contrails_max)

print(deltas_ATR_CO2_compromise)
print(deltas_ATR_CO2_max)

print(deltas_ATR_Total_compromise)
print(deltas_ATR_Total_max)

print(len(deltas_ATR_NOX_Ozone_compromise), len(deltas_ATR_NOX_Ozone_max), len(deltas_ATR_NOX_Methane_compromise), len(deltas_ATR_NOX_Methane_max), len(deltas_ATR_Water_Vapour_compromise), len(deltas_ATR_Water_Vapour_max), len(deltas_ATR_Contrails_compromise), len(deltas_ATR_Contrails_max), len(deltas_ATR_CO2_compromise), len(deltas_ATR_CO2_max), len(deltas_ATR_Total_compromise), len(deltas_ATR_Total_max))
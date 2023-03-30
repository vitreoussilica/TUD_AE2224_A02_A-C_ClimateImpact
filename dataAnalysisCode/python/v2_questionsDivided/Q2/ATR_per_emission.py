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
                    triplets.append((flight_trio[0], flight_trio[1], flight_trio[2]))
                    continue

mitigation_potentials_compromise = []
mitigation_potentials_max = []
negative_triplets = []

for triplet in triplets:
    ATRs = [triplet[0].total_ATR(), triplet[1].total_ATR(), triplet[2].total_ATR()]

    total0 = triplet[0].total_ATR()
    total1 = triplet[1].total_ATR()
    total2 = triplet[2].total_ATR()

    if total2 > 0 and total1 > 0:
        mitigation_potential_compromise =  -1 *  (1 - total1 / total2)
        mitigation_potential_max = -1 * (1 - total0 / total2) 
    elif total2 > 0 and total1 < 0:
        mitigation_potential_compromise = -1 + total1 / total2
        mitigation_potential_max = -1 + total0 / total2
    elif total2 > 0 and total0 < 0:
        mitigation_potential_compromise = -1 *  (1 - total1 / total2)
        mitigation_potential_max = -1 + total1 / total2
    elif total2 < 0 and total1 < 0  and total2 < 0:
        negative_triplets.append(triplet)


    mitigation_potentials_compromise.append(mitigation_potential_compromise)
    mitigation_potentials_max.append(mitigation_potential_max)


## Lists that include the mitigation potential for each flight
print(mitigation_potentials_compromise)
print(mitigation_potentials_max)

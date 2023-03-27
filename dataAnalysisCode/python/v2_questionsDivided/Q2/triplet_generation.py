import sys
sys.path.insert(1, '/Users/gerbendrijfhout/Desktop/Project/TUD_AE2224_A02_A-C_ClimateImpact/dataAnalysisCode/python/v1')

import flight as f
import retrieve_flight_data_general as fdg
import filenames as fn
import export_routes as er
import data_checks as checks
routes_list = er.all_route_coordinates()

## This function returns a list of all triplets of flights that are in the full_data directory
## This function forms the basis for the other functions in this file
def all_triplets():
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
                        if checks.is_full_set(flight_trio):
                            triplets.append((flight_trio[0], flight_trio[1], flight_trio[2]))
                        else:
                            print("Error: not a full set")
                        continue

    return triplets

## This function returns a list of all triplets in a certain month
def all_triplets_for_month(month: int):
    all_triplets_list = all_triplets()
    triplets_for_month = []

    for triplet in all_triplets_list:
        if triplet[0].datestamp == month:
            triplets_for_month.append(triplet)

    print(f'There are {len(triplets_for_month)} triplets in month {month}')
    return triplets_for_month

## This function returns a list of all triplets during daytime
def all_triplets_for_daytime():
    all_triplets_list = all_triplets()
    triplets_for_daytime = []

    for triplet in all_triplets_list:
        if triplet[0].time == 1:
            triplets_for_daytime.append(triplet)

    print(f'There are {len(triplets_for_daytime)} triplets during daytime')
    return triplets_for_daytime

## This function returns a list of all triplets during nighttime
def all_triplets_for_nighttime():
    all_triplets_list = all_triplets()
    triplets_for_nighttime = []

    for triplet in all_triplets_list:
        if triplet[0].time == 0:
            triplets_for_nighttime.append(triplet)

    print(f'There are {len(triplets_for_nighttime)} triplets during nighttime')
    return triplets_for_nighttime
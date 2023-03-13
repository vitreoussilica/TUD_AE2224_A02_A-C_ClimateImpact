import sys
sys.path.insert(1, '/Users/gerbendrijfhout/Desktop/Project/TUD_AE2224_A02_A-C_ClimateImpact/dataAnalysisCode/python/v1')

import flight as f
import retrieve_flight_data_general as fdg
import filenames as fn
import export_routes as er

import xarray as x

all_files = fn.all_filenames_airtraf_ac("/Users/gerbendrijfhout/Desktop/Project/Full_data")
all_flights = fdg.files_to_flight_objects(all_files)
routes_list = er.all_route_coordinates()

def total(flight: f.Flight, field: int):
    ATR_sum = 0.0
    for i in range(0, flight.data.shape[1]):
        ATR_sum += flight.data[field, i]

    print(ATR_sum)
    return ATR_sum

for i in range(0,12):
    filepaths = fn.all_filenames_for_month("/Users/gerbendrijfhout/Desktop/Project/Full_data", 'airtraf_ac.nc', i)
    print(i)
    flights_in_month = fdg.files_to_flight_objects(filepaths)

    for j in range(0, 31):
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
                for flight in flights_at_time:
                    if flight.route == routes_list[l]:
                        continue
                

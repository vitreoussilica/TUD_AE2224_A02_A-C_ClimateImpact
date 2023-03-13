import xarray as x
import find_airports as ap
import numpy as np
import filenames as fn
from flight import Flight

from os import listdir
from os.path import isfile, join

## The function below gives all routes in a given file that operate from one location to the other.
## Input for this function are the filename, and the location of the departure and arrival airport.
def get_route_data(filename, longitude1: float, latitude1: float, longitude2: float, latitude2: float):
    file = x.open_dataset(filename)
    data = file.variables['routes_out'].data

    flights = []

    for j in range(0,data[:,0,0,0].size):
        for i in range(0,100):
            if round(float(data[j,i,0,0]), 3) == round(longitude1, 3) and round(float(data[j,i,1,0]), 3) == round(latitude1, 3) and round(float(data[j,i,0,-1]), 3) == round(longitude2, 3) and round(float(data[j,i,1,-1]), 3) == round(latitude2, 3):

                route_data = data[j,i,:,:]
                # give the 20180101 field from the filename and adding it to route-datestamp

                route_datestamp = filename[-27:-19]
                route_day = j
                route_timestamp = filename[-47:-43]
                route_optimisation = filename[-41:-38]

                flight = Flight(route_data, route_datestamp, route_day, route_timestamp, route_optimisation)

                flights.append(flight)

    return flights

# print(get_route_data("../Project/Full_data/DT00/f100___________20180101_0000_airtraf_ac.nc", 4.4844, 50.9014, -3.5626, 40.4719))
def all_airtraf_ac_for_route(path_to_full_data: str, longitude1: float, latitude1: float, longitude2: float, latitude2: float):
    filepaths = fn.all_filenames_airtraf_ac(path_to_full_data)
    all_routes = []

    for filepath in filepaths:
        all_routes.append(get_route_data(path_to_full_data + filepath, longitude1, latitude1, longitude2, latitude2))

    return all_routes

## Example: This example prints all airtraf ac data for the route between Brussels and Madrid.
print(all_airtraf_ac_for_route("../Project/Full_data", 4.4844, 50.9014, -3.5626, 40.4719))

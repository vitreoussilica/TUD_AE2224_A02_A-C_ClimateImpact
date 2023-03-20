## This script exports all the routes from the f100___________20180101_0000_airtraf_ac.nc file to a text file.

import xarray as x
import find_airports as ap

data_ac = x.open_dataset("/Users/gerbendrijfhout/Desktop/Project/project_data/f100___________20180101_0000_airtraf_ac.nc")

data = data_ac.variables['routes_out'].data

def get_all_routes(file_data):
    routes = []
    for i in range(0,100):
        longitude1 = file_data[0,i,0,0]
        latitude1 = file_data[0,i,1,0]

        longitude2 = file_data[0,i,0,-1]
        latitude2 = file_data[0,i,1,-1]

        ap1, ap2 = ap.find_route_icao(float(longitude1), float(latitude1), float(longitude2), float(latitude2))
        route = (str(ap1), str(ap2), longitude1, latitude1, longitude2, latitude2)


        # Write code to append routes to a list of routes.
        routes.append(route)

        # Sort the routes list alphabetically based on the first entry of each tuple it contains
        routes.sort(key=lambda x: x[0])

    return routes

all_routes = get_all_routes(data)

# write a text file with all the routes. Each route is one line.
with open('routes.txt', 'w') as f:
    for route in all_routes:
        f.write(route[0] + ' ' + route[1] + ' ' + str(route[2]) + ' ' +  str(route[3]) + ' ' + str(route[4]) + ' ' + str(route[5]) +'\n')

def all_route_coordinates():
    list = []
    for route in all_routes:
        list.append((route[2], route[3], route[4], route[5]))

    return list



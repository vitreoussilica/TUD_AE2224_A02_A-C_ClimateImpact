import filenames as fn
import xarray as x
from flight import Flight

def files_to_flight_objects(filenames: list):
    flights = []

    for f in filenames:
        file = x.open_dataset(f)
        data = file.variables['routes_out'].data

        if f[-27:-23] == "2019":
            continue

        for j in range(0,data[:,0,0,0].size):
            for i in range(0,100):
                route_data = data[j,i,:,:]

                ## Route_datestamp contains the month as an integer
                ## December 2017 is month 0, January 2018 is month 1, etc.
                if f[-27:-23] == "2017":
                    route_datestamp = 0
                elif f[-27:-23] == "2018":
                    route_datestamp =  int(f[-23:-21])
                else:
                    print("Error: route datestamp not found")

                route_day = int(f[-21:-19]) + j - 1

                ## Setting the timestamp to 0 for DT00, 1 for DT12
                if f[-47:-43] == "DT12":
                    route_timestamp = 1
                elif f[-47:-43] == "DT00":
                    route_timestamp = 0
                else:
                    print("Error: route timestamp not found")
                ##route_timestamp = f[-47:-43]

                ## Setting the route optimisation to 0 for cost optimal, 1 for compromise, 2 for climate optimal
                if f[-41:-38] == "100":
                    route_optimisation = 2
                    ## Climate optimal
                elif f[-41:-38] == "10_":
                    route_optimisation = 1
                    ## Compromise Solution +1% SOC
                elif f[-41:-38] == "00_":
                    route_optimisation = 0
                    ## Cost optimal
                else:
                    print("Error: route optimisation not found")
                ## route_optimisation = f[-41:-38]

                route_coordinates = (route_data[0,0], route_data[1,0], route_data[0,-1], route_data[1,-1])
                flight = Flight(route_data, route_datestamp, route_day, route_timestamp, route_optimisation, route_coordinates)

                flights.append(flight)

    return flights
import filenames as fn
import xarray as x
from flight import Flight

def files_to_flight_objects(filenames: list):
    flights = []

    for f in filenames:
        file = x.open_dataset(f)
        data = file.variables['routes_out'].data

        for j in range(0,data[:,0,0,0].size):
            for i in range(0,100):
                route_data = data[j,i,:,:]
                route_datestamp = f[-27:-19]
                route_day = j
                route_timestamp = f[-47:-43]
                route_optimisation = f[-41:-38]

                flight = Flight(route_data, route_datestamp, route_day, route_timestamp, route_optimisation)

                flights.append(flight)

    return flights
import xarray as x
from flight import Flight
import filenames as fn
import retrieve_flight_data_general as fdg


## Not sure this works, lol...
def total_ATR(flights: list):
    total = 0.0
    print(len(flights))
    for flight in flights:
        total += flight.total_ATR()

    return total

print(total_ATR(fdg.files_to_flight_objects(fn.all_filenames_airtraf_ac("../Project/Full_data"))))

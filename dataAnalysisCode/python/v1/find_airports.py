import airportsdata

airports = airportsdata.load()

# Find the airport name for a given longitude and latitude
def find_airport_name(longitude, latitude):
    for airport_key in airports:
        airport = airports[airport_key]
        rounded_lon = round(airport['lon'], 3)
        rounded_longitude = round(longitude, 3)
        rounded_lat = round(airport['lat'], 3)
        rounded_latitude = round(latitude, 3)

        if (rounded_longitude - 0.1 <= rounded_lon < rounded_longitude + 0.1) and (rounded_latitude - 0.1 <= rounded_lat < rounded_latitude + 0.1):
            return airport['name']
    coordinate_string = f'{round(longitude, 3)}, {round(latitude, 3)}'
    return coordinate_string

# Find the airport (aiports-data dictionary) for a given longitude and latitude   
def find_airport(longitude, latitude):
    for airport_key in airports:
        airport = airports[airport_key]
        rounded_lon = round(airport['lon'], 3)
        rounded_longitude = round(longitude, 3)
        rounded_lat = round(airport['lat'], 3)
        rounded_latitude = round(latitude, 3)
        if (rounded_longitude - 0.1 <= rounded_lon < rounded_longitude + 0.1) and (rounded_latitude - 0.1 <= rounded_lat < rounded_latitude + 0.1):
            return airport
    coordinate_string = f'{round(longitude, 3)}, {round(latitude, 3)}'
    return coordinate_string

# Find the airport ICAO for a given longitude and latitude
def find_airport_icao(longitude, latitude):
    for airport_key in airports:
        airport = airports[airport_key]
        rounded_lon = round(airport['lon'], 3)
        rounded_longitude = round(longitude, 3)
        rounded_lat = round(airport['lat'], 3)
        rounded_latitude = round(latitude, 3)

        if (rounded_longitude - 0.1 <= rounded_lon < rounded_longitude + 0.1) and (rounded_latitude - 0.1 <= rounded_lat < rounded_latitude + 0.1):
            return airport['icao']
    coordinate_string = f'{longitude}, {latitude}'
    return coordinate_string
    
# Find the airport IATA for a given longitude and latitude
def find_airport_iata(longitude, latitude):
    for airport_key in airports:
        airport = airports[airport_key]
        rounded_lon = round(airport['lon'], 3)
        rounded_longitude = round(longitude, 3)
        rounded_lat = round(airport['lat'], 3)
        rounded_latitude = round(latitude, 3)
        if (rounded_longitude - 0.1 <= rounded_lon < rounded_longitude + 0.1) and (rounded_latitude - 0.1 <= rounded_lat < rounded_latitude + 0.1):
            return airport['iata']
    coordinate_string = f'{round(longitude, 3)}, {round(latitude, 3)}'
    return coordinate_string

# Find the ICAO codes for the airports between two given longitudes and latitudes
def find_route_icao(longitude, latitude, longitude2, latitude2):
    airport_icao = find_airport_icao(longitude, latitude)
    airport_icao2 = find_airport_icao(longitude2, latitude2)
    return airport_icao, airport_icao2

def find_route_iata(longitude, latitude, longitude2, latitude2):
    airport_iata = find_airport_iata(longitude, latitude)
    airport_iata2 = find_airport_iata(longitude2, latitude2)
    return airport_iata, airport_iata2

# Find the names for the airports between two given longitudes and latitudes
def find_route_name(longitude, latitude, longitude2, latitude2):
    airport_name = find_airport_name(longitude, latitude)
    airport_name2 = find_airport_name(longitude2, latitude2)
    return airport_name, airport_name2

# Find the airports (aiports-data dictionaries) between two given longitudes and latitudes
def find_route_airport(longitude, latitude, longitude2, latitude2):
    airport = find_airport(longitude, latitude)
    airport2 = find_airport(longitude2, latitude2)
    return airport, airport2


## Example usage
##find_route_icao(28.7519, 41.2753, 4.7639, 52.3086)
##find_route_name(28.7519, 41.2753, 4.7639, 52.3086)
##find_route_airport(28.7519, 41.2753, 4.7639, 52.3086)

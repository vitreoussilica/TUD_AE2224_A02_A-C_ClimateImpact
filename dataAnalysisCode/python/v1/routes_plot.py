import plotly.graph_objects as go
import pandas as pd
import xarray as x

data_ac = x.open_dataset("/Users/gerbendrijfhout/Desktop/Project/project_data/f100___________20180101_0000_airtraf_ac.nc")
routes = data_ac.variables['routes_out']


""""
df_airports = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
df_airports.head()
"""

# write a function that creates a CSV file with the start and end points of the routes
# and the corresponding lat and long
# this is the input for the plotly scattergeo function
dep_long = routes.data[0,:,0,0]
dep_lat = routes.data[0,:,1,0]

arr_long = routes.data[0,:,0,-1]
arr_lat = routes.data[0,:,1,-1]

df_flight_paths = pd.DataFrame({'start_lon': dep_long, 'start_lat': dep_lat, 'end_lon': arr_long, 'end_lat': arr_lat})
df_flight_paths.head()

fig = go.Figure()


flight_paths = []
for i in range(len(df_flight_paths)):
    fig.add_trace(
        go.Scattergeo(
            locationmode = 'geojson-id',
            lon = [df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i]],
            lat = [df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i]],
            mode = 'lines',
            line = dict(width = 1,color = 'red'),
            opacity = float(0.9),
        )
    )

    fig.add_trace(go.Scattergeo(
        locationmode = 'geojson-id',
        lon = [df_flight_paths['end_lon'][i]],
        lat = [df_flight_paths['end_lat'][i]],
        mode='markers',
        marker=dict(
            size=8,
            color='rgb(255, 0, 0)',
            line=dict(
                width=3,
                color='rgba(68, 68, 68, 0)'
            )
        )
    ))

fig.update_layout(
    title_text = 'Europe Flights',
    showlegend = False,
    geo = dict(
        scope = 'europe',
        projection_type = 'azimuthal equal area',
        showland = True,
        landcolor = 'rgb(243, 243, 243)',
        countrycolor = 'rgb(204, 204, 204)',
    ),
)

fig.show()
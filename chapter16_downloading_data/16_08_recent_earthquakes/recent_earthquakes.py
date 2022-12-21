import json
from plotly import offline
from plotly.graph_objs import Scattergeo, Layout


# 4.5+ magnitude earthquakes from the last 30 days. (date 12.21.2022)
# source: https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

filename = 'data/4.5_month.geojson'

# read into json loader
with open(filename, encoding="utf8") as f:
    all_eq_data = json.load(f)

# init magnitudes, longitudes, tsunamis, latitudes and text list. extract title
mags, lons, lats, hover_texts, tsunamis = [], [], [], [], []
title = all_eq_data['metadata']['title']

# append data into lists
for eq in all_eq_data['features']:
    mags.append(eq['properties']['mag'])
    lons.append(eq['geometry']['coordinates'][0])
    lats.append(eq['geometry']['coordinates'][1])
    hover_texts.append(eq['properties']['title'])
    tsunamis.append(eq['properties']['tsunami'])

# if tsunami caused (1), use square symbol, otherwise circle
symbols = ['circle', 'square']

# configure data for Plotly chart
data = {
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        # marker size is 5*magnitude
        'size': [mag*5 for mag in mags],
        # color is magnitude list
        'color': mags,
        'colorscale': 'Magma',
        'reversescale': True,
        # legend
        'colorbar': {'title': 'Magnitude'},
        # use square symbol if earthquake caused tsunami
        'symbol': [symbols[tsunami] for tsunami in tsunamis]
    }

}

# layout takes only title as argument
my_layout = Layout(title=title)

# figure data and layout, plot
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
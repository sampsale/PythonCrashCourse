import json
from plotly import offline
from plotly.graph_objs import Scattergeo, Layout

filename = 'data/eq_data_30_day_m1.json'
# open file with json loader
with open(filename) as f:
    all_eq_data = json.load(f)

# extract the earthquake dictionaries and init lists, extract title
all_eq_dicts = all_eq_data['features']
mags = []
lons = []
lats = []
hover_texts = []
title = all_eq_data['metadata']['title']

# append data to lists
for eq in all_eq_dicts:
    mags.append(eq['properties']['mag'])
    lons.append(eq['geometry']['coordinates'][0])
    lats.append(eq['geometry']['coordinates'][1])
    hover_texts.append(eq['properties']['title'])

# configure data for Plotly chart
data = {
    # type is geographical "scatterplot"
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        # marker size is 5*magnitude
        'size': [mag*5 for mag in mags],
        # color is magnitude list
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        # legend
        'colorbar': {'title': 'Magnitude'}

    }
}
# layout takes only title as argument
my_layout = Layout(title=title)

# figure data and layout, plot
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

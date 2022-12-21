import csv
from plotly import offline
from plotly.graph_objs import Scattergeo, Layout


# all fires detectable by satellite on 09.22.2018
filename = 'data/world_fires_1_day.csv'

# open file
with open(filename) as f:
    # read into csv reader
    reader = csv.DictReader(f)
    # init lists for brightness, lats and longs
    brightnesses, lats, longs = [], [], []
    # loop through rows
    for row in reader:
        brightnesses.append(float(row['brightness']))
        lats.append(row['latitude'])
        longs.append(row['longitude'])

# configure data for Plotly chart
data = {
    'type': 'scattergeo',
    'lat': lats,
    'lon': longs,
    'marker': {
        'size': [brightness/25 for brightness in brightnesses],
        # color is brightness list
        'color': brightnesses,
        'colorscale': 'Magma',
        'reversescale': True,
        # legend
        'colorbar': {'title': 'Brightness'}
    }
}

# layout takes only title as argument
my_layout = Layout(title='Global fires on 09/22/2018')

# figure data and layout, plot
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
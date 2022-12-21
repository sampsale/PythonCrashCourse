# data from https://en.ilmatieteenlaitos.fi/download-observations
# GET RAINFALL AND SNOW DEPTH BY DAY IN HELSINKI

import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/weather_data_helsinki_2021.csv'

# open file
with open(filename) as f:
    # read into csv reader
    reader = csv.DictReader(f)

    rainfall, snow_depth, dates = [], [], []

    # loop through rows
    for row in reader:
        # try except block just in case there's errors in data
        try:
            # get the columns we are interested in. '-' stands for 0 in this dataset so account for that
            # dataset also has -1 for precipation sometimes, that I can't really explain so I'll set those as 0 as well
            if row['Precipitation amount (mm)'] == '-' or row['Precipitation amount (mm)'] == '-1':
                rain = 0
            else:
                rain = float(row['Precipitation amount (mm)'])
            if row['Snow depth (cm)'] == '-':
                snow = 0
            else:
                # convert CM to MM
                snow = (float(row['Snow depth (cm)'])) / 10
            # Year, m, d are the columns we want for date
            date = datetime.strptime(
                f"{row['Year']}-{row['m']}-{row['d']}", '%Y-%m-%d')

        except:
            print('Something went wrong')
        else:
            rainfall.append(rain)
            snow_depth.append(snow)
            dates.append(date)


# init plot
plt.style.use('bmh')
fig, ax = plt.subplots(figsize=(15, 8))

# plot the rainfall and snow depth
ax.plot(dates, rainfall, c='cyan', label='Rainfall (mm)', alpha=0.8)
ax.bar(dates, snow_depth, color='red',  label='Snow depth (mm)', alpha=0.7)

# styling
ax.set_title('Daily rain- or snowfall in Helsinki, 2021', fontsize=30)
ax.set_ylabel('MM', fontsize=25)
ax.set_xlabel('Date', fontsize=25)
ax.margins(x=0, y=0)
ax.legend()

# format dates (x)
fig.autofmt_xdate()

plt.show()

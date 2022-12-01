import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'

# open file
with open(filename) as f:
    # read into csv reader
    reader = csv.DictReader(f)

    rain_days, dates = [], []
    
    # loop through rows
    for row in reader:
        # try except block just in case there's errors in data
        try:
            # PRCP (precipation) is the column we want for rain days
            rain_day = float(row['PRCP'])
            # DATE is the column we want for date
            date = datetime.strptime(row['DATE'], '%Y-%m-%d')
        except: 
            print(f'Something went wrong with row {row}')
        else:
            rain_days.append(rain_day)
            dates.append(date)
        



# init plot
plt.style.use('bmh')
fig, ax = plt.subplots(figsize=(15,8))


# plot the rain
ax.plot(dates, rain_days, c='blue')

# styling
ax.set_title('Daily rain in Sitka, 2018', fontsize=30)
ax.set_ylabel('Rain (inches)', fontsize=25)
ax.set_xlabel('Date', fontsize=25)
ax.margins(x=0, y=0)

# format dates (x)
fig.autofmt_xdate()

plt.show()
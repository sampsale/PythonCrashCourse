import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/san_francisco_weather_2021.csv'

# open file
with open(filename) as f:
    # read into csv reader
    reader = csv.DictReader(f)

    highs, lows, dates = [], [], []
    
    # loop through rows
    for row in reader:
        # try except block just in case there's errors in data
        try:
            # TMAX & TMIN  are the columns we want for min and max temparature
            high = int(row['TMAX'])
            low = int(row['TMIN'])
            # DATE is the column we want for date
            date = datetime.strptime(row['DATE'], '%Y-%m-%d')
        except: 
            pass
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)
        



# plot everything
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(15, 8))
ax.plot(dates, highs, c='#fc1786', label='Highs')
ax.plot(dates, lows, c='#1f77b4', label='Lows')

# styling
ax.set_title(
    'Daily highs and lows in San Francisco, 2021', fontsize=30)
ax.set_ylabel('Temperature (F)')
ax.set_xlabel('Date', fontsize=2)
ax.legend()
fig.autofmt_xdate()
ax.margins(x=0, y=0)

# show
plt.show()

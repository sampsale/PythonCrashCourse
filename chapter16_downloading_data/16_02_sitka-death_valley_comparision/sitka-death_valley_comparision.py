import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename_death_valley = 'data/death_valley_2018_simple.csv'
filename_sitka = 'data/sitka_weather_2018_simple.csv'


def get_temperatures(filename):
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
                print(f'Something went wrong with row {row}')
            else:
                highs.append(high)
                lows.append(low)
                dates.append(date)
    return highs, lows, dates


# get data for both locations
death_valley_highs, death_valley_lows, death_valley_dates = get_temperatures(
    filename_death_valley)
sitka_highs, sitka_lows, sitka_dates = get_temperatures(filename_sitka)


# plot everything
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(15, 8))
ax.plot(death_valley_dates, death_valley_highs, c='#fc1786', label='Death Valley Highs')
ax.plot(death_valley_dates, death_valley_lows, c='#1f77b4', label='Death Valley Lows')
ax.plot(sitka_dates, sitka_highs, c='#a10864', label='Sitka Highs')
ax.plot(sitka_dates, sitka_lows, c='#030740', label='Sitka Lows')

# styling
ax.set_title(
    'Daily highs and lows in Sitka and Death Valley (F), 2018', fontsize=30)
ax.set_ylabel('Temperature (F)')
ax.set_xlabel('Date', fontsize=2)
ax.legend()
fig.autofmt_xdate()
ax.margins(x=0, y=0)

# show
plt.show()

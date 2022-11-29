from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline


# die with 6 sides
die = Die()
results = []

# roll 3 dice 10000 times
for roll_num in range(10000):
    results.append(die.roll() + die.roll() + die.roll())



# max_result of rolling these particular dice
max_result = die.num_sides*3

# count frequencies of results
frequencies = []
for result in range(3, max_result+1):
    frequency=results.count(result)
    frequencies.append(frequency)

# make list of possible result values for plotly Bar
x_values = list(range(3, max_result+1))
# give data to Bar
data = Bar(x=x_values, y=frequencies)

# titles and tickers for axis
y_axis_config = {'title': 'Frequency'}
x_axis_config = {'title': 'Result', 'dtick': 1}

# layout for plotly
my_layout = Layout(title='Results of rolling three dice 10000 times', xaxis=x_axis_config, yaxis=y_axis_config)
# plot offline
offline.plot({'data': data, 'layout': my_layout}, filename='d6timesthree.html')
from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline


# die with 6 sides
die = Die()
results = []

# roll 2 dice 10000 times AND multiply the results with each other
for roll_num in range(10000):
    results.append(die.roll() * die.roll())

# # optional list comprehension method
# results = [die.roll() * die.roll() for roll_num  in range(10000)]

# max_result of rolling these particular dice
max_result = die.num_sides * die.num_sides

# count frequencies of results
frequencies = []
for result in range(2, max_result+1):
    frequency=results.count(result)
    frequencies.append(frequency)

# make list of possible result values for plotly Bar
x_values = list(range(2, max_result+1))
# give data to Bar
data = Bar(x=x_values, y=frequencies)

# titles and tickers for axis
y_axis_config = {'title': 'Frequency'}
x_axis_config = {'title': 'Result', 'dtick': 1}

# layout for plotly
my_layout = Layout(title='Results of rolling two dice and multiplying 10000 times', xaxis=x_axis_config, yaxis=y_axis_config)
# plot offline
offline.plot({'data': data, 'layout': my_layout}, filename='d6timestwomultiplied.html')
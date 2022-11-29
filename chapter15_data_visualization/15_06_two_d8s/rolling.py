from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline


# two dice with 8 sides
die1 = Die(8)
die2 = Die(8)

results = []

# roll 10000 times
for roll_num in range(10000):
    result1 = die1.roll()
    result2 = die2.roll()
    results.append(result1+result2)



# max_result of rolling these particular dice
max_result = die1.num_sides + die2.num_sides

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
my_layout = Layout(title='Results of rolling two D8 10000 times', xaxis=x_axis_config, yaxis=y_axis_config)
# plot offline
offline.plot({'data': data, 'layout': my_layout}, filename='d8.html')
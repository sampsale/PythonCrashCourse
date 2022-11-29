
from die import Die
import matplotlib.pyplot as plt

# die with 6 sides
die = Die()

results = []
# roll 2 dice 10000 times and add to results
for roll_num in range(10000):
    results.append(die.roll() + die.roll())

# max result is 2*number of sides
max_result = die.num_sides * 2

# plot histogram, results as X and possible results as bins
plt.hist(results, bins=range(2,14))
plt.xlabel('Result')
plt.ylabel('Frequency')
plt.xticks(range(2,13))
plt.title('Result of throwing two six sided dice 10000 times')
plt.show()

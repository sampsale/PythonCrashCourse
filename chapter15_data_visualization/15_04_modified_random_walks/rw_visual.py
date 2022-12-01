from random import choice
import matplotlib.pyplot as plt
from randomwalk import RandomWalk


rw = RandomWalk(50000)
rw.fill_walk()

# use classic sctyle
plt.style.use('classic')

# init fig and ax
fig, ax = plt.subplots(figsize=(18, 10))
ax.set_title('Random walks', fontsize=34)
# hide axis
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# 0-max num_points
point_numbers = range(rw.num_points)

# scatter the values
# ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
#            cmap=plt.cm.Blues, edgecolors='none', s=1)

# plot the values
ax.plot(rw.x_values, rw.y_values, linewidth=0.8)

# scatter the starting and ending points
ax.scatter(0, 0, c='green', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

# show
plt.show()

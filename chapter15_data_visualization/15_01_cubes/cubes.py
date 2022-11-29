import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


# cubes and input values
# cubes for y, input for x
x_values = range(1, 1001)
y_values = [x**3 for x in x_values]
print(len(x_values))
print(len(y_values))
plt.style.use('bmh')
# generate plot
fig, ax = plt.subplots()
fig.set_size_inches(16, 8)
# plot for line
#ax.plot(x_values, y_values, linewidth=3)
# scatter for dots
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# labels
ax.set_title('Cubes', fontsize=34)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.0f'))


ax.axis([min(x_values), (max(x_values) + max(x_values)/10), min(y_values), (max(y_values) + max(y_values)/20)])

ax.tick_params(axis='both', labelsize=14)

# plt.savefig('testplot.png', bbox_inches='tight')
plt.show()

import matplotlib.pyplot as plt

x_values = range(1, 1001, 10)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, color='red', s=15)
# ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)  # color in RGB model
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.YlGnBu, s=25)  # Colormap

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)
ax.ticklabel_format(style='plain')

# Set the range for each axis.
ax.axis([-10, 1100, -10000, 1_100_000])  # [xmin, xmax, ymin, ymax]

# plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
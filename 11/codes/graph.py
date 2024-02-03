import matplotlib.pyplot as plt
import numpy as np

# Read data from file
data = np.loadtxt("data.txt")

# Extract x and y values
x_n = data[:, 0]
y_n = data[:, 1]

# Plotting the graph
plt.plot(x_n, y_n, marker='o')
plt.title('Stem plot of y(n)')
plt.xlabel('x(n)')
plt.ylabel('y(n)')
plt.xticks(np.arange(0, len(x_n), 2))  # Setting x-axis scale to 2
plt.grid(True)
plt.show()
plt.save()

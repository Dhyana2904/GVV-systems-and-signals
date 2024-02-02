import matplotlib.pyplot as plt
import numpy as np

# Read data from file
data = np.loadtxt("data.txt")

# Extract x and y values
x_values = data[:, 0]
y_values = data[:, 1]

# Plotting the graph
plt.plot(x_values, y_values, marker='o')
plt.title('Stem plot of s(n)')
plt.xlabel('Number of Terms (n)')
plt.ylabel('Sum of n Terms')
plt.xticks(np.arange(0, len(x_values), 2))  # Setting x-axis scale to 2
plt.grid(True)
plt.show()


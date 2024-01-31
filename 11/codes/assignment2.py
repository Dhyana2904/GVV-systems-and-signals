import matplotlib.pyplot as plt
import numpy as np

# Geometric progression parameters
a = 0.15
r = 0.1
n_terms = 20

# Function to calculate the sum of the first n terms
def geometric_sum(n):
    return a * ((r**(n+1) - 1) / (r - 1))

# Generate x values
x_values = np.arange(0, n_terms + 1, 1)

# Generate y values using the geometric_sum function
y_values = [geometric_sum(n) for n in x_values]

# Plotting the graph
plt.plot(x_values, y_values, marker='o')
plt.title('Stem plot of s(n)')
plt.xlabel('Number of Terms (n)')
plt.ylabel('Sum of n Terms')
plt.xticks(np.arange(0, n_terms + 1, 2))  # Setting x-axis scale to 2
plt.grid(True)
plt.show()

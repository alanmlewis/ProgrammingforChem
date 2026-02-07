# Load libraries
import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data = np.loadtxt('activity.txt')

# x axis points are the first row, excluding the first number
x = data[0,1:]
# y axis points are the first column, excluding the first number
y = data[1:,0]
# z values are the remainder of the grid
z = data[1:,1:]

# Create the contour plot
plt.contour(x,y,z,levels=10)

# Save the contour plot
plt.savefig('contour.png')

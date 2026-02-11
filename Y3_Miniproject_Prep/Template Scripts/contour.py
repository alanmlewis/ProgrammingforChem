import numpy as np
import matplotlib.pyplot as plt

# Load the data into a variable
data = np.loadtxt('activity.txt')

# The first row of the data, excluding the first value, are the range of x values.
x = data[0,1:]
# The first column of the data, excluding the first value, are the range of y values.
y = data[1:,0]
# The remainder of the dataset (i.e. excluding the first row and column) contains the values we want to plot
z = data[1:,1:]

# Create a filled contour plot
plt.contourf(x, y, z, levels=20, cmap='inferno')

# Add axis labels and a title
plt.xlabel('Temperature / °C')
plt.ylabel('pH')
plt.title('Enzyme Activity (%)')

# Add a colourbar so we can interpret the colours
plt.colorbar()

# Save the resulting figure
plt.savefig('contour.png',bbox_inches='tight',dpi=500)

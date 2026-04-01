# Load libraries
import numpy as np
import matplotlib.pyplot as plt

# Load data from file
veh = np.loadtxt('vehicular.txt',skiprows=1)

# Plot a line graph using the first and second columns of the loaded data
plt.plot(veh[:,0],veh[:,1],label='Vehicular Emissions')

# Set an x- and y-axis label, and a legend
plt.xlabel('% Change in Emissions')
plt.ylabel('% Change in Ozone Conc.')
plt.legend()

# Save the plot
plt.savefig('errorbars.png')

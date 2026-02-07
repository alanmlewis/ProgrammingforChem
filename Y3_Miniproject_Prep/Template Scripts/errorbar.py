import numpy as np
import matplotlib.pyplot as plt

# Load data from three different files into three different variables
veh = np.loadtxt('vehicular.txt',skiprows=1)
paint = np.loadtxt('paint.txt',skiprows=1)
solvents = np.loadtxt('solvents.txt',skiprows=1)

# Plot each line with errorbars (yerr), adding a cap to the end of the errorbars
plt.errorbar(veh[:,0], veh[:,1], yerr=veh[:,2], label='Vehicular Emissions', capsize=3, fmt='x-')
plt.errorbar(solvents[:,0], solvents[:,1], yerr=solvents[:,2], label='Non-Paint Solvents', capsize=3, fmt='o--')
plt.errorbar(paint[:,0], paint[:,1], yerr=paint[:,2], label='Paint Solvents', capsize=3, fmt='^:')

# Add axis labels and a legend to the plot
plt.xlabel('% Change in Emissions')
plt.ylabel('% Change in Ozone Conc.')
plt.legend()

# Save the figure
plt.savefig('errorbar.png')

import numpy as np
import matplotlib.pyplot as plt

# Set font size
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 16}
plt.rc('font', **font)

# Load the data, skipping the first row as it contains text column header
data = np.loadtxt('olive_oil.csv',skiprows=1,delimiter=',')

# Select only the 6th column
oleic = data[:,5]

# Plot and save the bar chart
plt.hist(oleic,edgecolor='black',bins=[55,57.5,60,62.5,65,67.5,70,72.5,75,77.5,80])
plt.xlabel('Oleic Acid Content (% of Fatty Acids)')
plt.ylabel('Count')

# Save the figure. bbox_inches sets the borders automatically, and dpi sets the resolution of the image
plt.savefig('histogram.png',bbox_inches='tight',dpi=500)

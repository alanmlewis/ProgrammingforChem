import pandas as pd
import matplotlib.pyplot as plt

# Set font size
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 16}
plt.rc('font', **font)

# Read the data file using pandas
protein = pd.read_csv('protein.csv')
# The x values are the time in hours
# Pandas using column headings to refer to columns of data
x = protein['hours']

# Plot the concentration of each different protein
for i in ['Asx','Glx','Leu']:
    plt.scatter(x, protein[i], label=i)

# Add axis labels and a legend to the plot
plt.xlabel('Time / hours')
plt.ylabel('Concentration / picomoles mg$^{-1}$')
plt.legend()

# Save the figure. bbox_inches sets the borders automatically, and dpi sets the resolution of the image
plt.savefig('scatter.png',bbox_inches='tight',dpi=500)

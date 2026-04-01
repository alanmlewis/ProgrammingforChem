import pandas as pd
import matplotlib.pyplot as plt

# Set font size
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 16}
plt.rc('font', **font)

protein = pd.read_csv('protein.csv')
x = protein['hours']

# Plot each line with errorbars (yerr), adding a cap to the end of the errorbars
for i in ['Asx','Glx','Leu']:
    plt.scatter(x, protein[i], label=i)

# Add axis labels and a legend to the plot
plt.xlabel('Time / hours')
plt.ylabel('Concentration / picomoles mg$^{-1}$')
plt.legend()

# Save the figure. bbox_inches sets the borders automatically, and dpi sets the resolution of the image
plt.savefig('scatter.png',bbox_inches='tight',dpi=500)

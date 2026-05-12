import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set font size
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 14}
plt.rc('font', **font)


# Load data on maths skills confidence
confidence_counts = pd.read_csv('maths_skills_processed.csv',index_col=0)

# Print the data to be plotted
print(confidence_counts)

# Get a list of column headings to put on the x axis
labels = confidence_counts.keys()
# Set the width of the bars to plot
width = 0.5
# Create an array of zeros, with one per column of data
bottom = np.zeros(len(labels))

# Loop over every row in the data set
# The data is in variable row, the row label in variable index
for index, row in confidence_counts.iterrows():
    # Create a bar chart using the column headings as the labels for each bar,
    # the data in row as the height of the bar, and the row label as the legend
    # The bottom of the bars is set by the array bottom, initially 0
    p = plt.bar(labels, row, width, label=index, bottom=bottom)
    # Add the heights of the bar to the variable bottom,
    # so the next bar will plotted directly on top of it
    bottom += row

# Add a title to the graph
plt.title("Distribution of confidence levels in different maths skills")
# Position the legend below the graph
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),ncol=2)

# Save the figure
plt.savefig('stacked_bar.png',bbox_inches='tight',dpi=500)

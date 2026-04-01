import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set font size
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 14}
plt.rc('font', **font)

# Load the data, skipping the first row as it contains text column header
data = np.loadtxt('olive_oil.csv',skiprows=1,delimiter=',')
# Load the column headings, as we will need them to label the graph
headers = pd.read_csv('olive_oil.csv').keys()

# Calculate the average for each column
av = np.average(data,axis=0)
# Sort the averages into descending order, and sort the headers in the same way
idx = np.argsort(av)[::-1]
av = av[idx]
headers = headers[idx]

# This will group every acid which has a lower than 5% content into a group called "Other"
cutoff = 5
# Selects only the averages where the average content is greater than 5%
selected_av = [av[i] for i in range(len(av)) if av[i] > cutoff]
# Selects only the headers where the average content is greater than 5%
selected_headers = [headers[i] for i in range(len(av)) if av[i] > cutoff]
# Adds a value to the list of averages which is the remaining percentage not covered by the selected values
selected_av.append(100-np.sum(selected_av))
# Adds a header to describe this "other" category
selected_headers.append('Other Fatty Acids')

# Plot and save the pie chart
plt.pie(selected_av,labels=selected_headers,labeldistance=None)
# Add a legend
plt.legend()
# Ad a title
plt.title('Average fatty acid content of olive oils')

# Save the figure. bbox_inches sets the borders automatically, and dpi sets the resolution of the image
plt.savefig('pie.png',bbox_inches='tight',dpi=500)

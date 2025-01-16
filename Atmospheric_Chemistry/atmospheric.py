import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# This section of code reads and prepares the data
# You don't need to modify it for today's workshop
# ------------------------------------------------------------------------------------
data = pd.read_csv('stoke.csv', skiprows=10)

data['Date'] = pd.to_datetime(data['Date'])
data['Time'] = data['Time'].replace('24:00:00','00:00:00')
data['Time'] = pd.to_datetime(data['Time']).dt.hour
data['Time'] = data['Time'].replace(0,24)

data = data.replace('No data',np.nan)
data = data.astype({'Nitrogen dioxide' : float, 'Nitric oxide' : float, 'Ozone' : float})

L = ['year', 'month', 'day', 'dayofweek', 'dayofyear']
date_gen = (getattr(data['Date'].dt, i).rename(i) for i in L)
data = data.join(pd.concat(date_gen, axis=1))
# ------------------------------------------------------------------------------------

# Plotting our first graph - the concentrations of NO, NO2, and O3 over time on December 1st 2017

# Get the subset of data which corresponds to December 2017
data_subset = data.loc[(data['month']==12)]
data_subset = data_subset.loc[(data_subset['year']==2017)]

# Get the Nitrogen dioxide data from the 1st of Decemeber 2017
plot_data = data_subset.loc[data_subset['day']==1]
x = plot_data['Time'].values
y = plot_data['Nitrogen dioxide'].values

# Create plot of x against y
plt.plot(x,y,label='label')

# Decorate the plot
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Title')
plt.legend()

# Save the plot
plt.savefig('plot1.png')
plt.close()

# ------------------------------------------------------------------------------------

# Plotting our second graph - average concentrations of NO, NO2, and O3 throughout the day in December 2017

# The x axis will be the same for each day
x = data_subset.loc[data_subset['day']==1]['Time'].values
# Create a variable which will contain the average NO2 concentration
y_no2 = 0
# Create a loop - the variable "day" will equal 1 to 31 in turn.
for day in range(1,32):
    plot_data = data_subset.loc[data_subset['day']==day]
    y_no2 = y_no2 + plot_data['Nitrogen dioxide'].values

y_no2 = y_no2/31

# Add the code to create, decorate, and save the graph here.



# ------------------------------------------------------------------------------------

# Plotting our third graph - average concentrations of NO, NO2, and O3 on each day in December 2017
# As a starting point, copy the code you used to plot the second graph and paste it below. Modify it to get the graph we want.




# ------------------------------------------------------------------------------------

# Plotting our fourth graph - the average concentrations of NO2 on each day in April 2017 and April 2020



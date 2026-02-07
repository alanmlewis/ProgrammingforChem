import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data using pandas, as it contains mixed data types (numbers and strings)
data = pd.read_csv('green.csv')

# Create new variable containing only the rows of the database where TEA is the base
tea = data[data['Base']=='TEA']
# Create new variable containing only a list of yields, when TEA was used as the base.
tea_yield = tea['Yield (%)'].values

# As above, but for DIPEA
dipea = data[data['Base']=='DIPEA']
dipea_yield = dipea['Yield (%)'].values

# Create boxplots for each base, by passing both datasets as a list into the boxplot function
plt.boxplot([tea_yield,dipea_yield],tick_labels=['TEA','DIPEA'])
plt.xlabel('Base')
plt.ylabel('Yield (%)')

plt.savefig('boxplot.png')


# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data = pd.read_csv('green.csv')
# Select only rows where the base is TEA
tea = data[data['Base']=='TEA']
# Create a new variable where containing all the yields when TEA is the base
tea_yield = tea['Yield (%)'].values

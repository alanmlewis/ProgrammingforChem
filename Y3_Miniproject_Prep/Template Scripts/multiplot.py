import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('green.csv')

etoac = data[data['Solvent']=='EtOAc']
etoac_yield = etoac['Yield (%)'].values
etoac_ee = etoac['Enantiomeric Excess (%)'].values

cpme = data[data['Solvent']=='CPME']
cpme_yield = cpme['Yield (%)'].values
cpme_ee = cpme['Enantiomeric Excess (%)'].values

fig, ax = plt.subplots(1,2)

ax[1].scatter(cpme_yield,cpme_ee)
ax[0].scatter(etoac_yield,etoac_ee)

ax[0].set_xlabel('Yield (%)')
ax[1].set_xlabel('Yield (%)')
ax[0].set_title('EtOAc')

plt.savefig('multiplot.png')

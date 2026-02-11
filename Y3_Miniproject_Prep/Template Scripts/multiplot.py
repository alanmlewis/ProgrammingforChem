import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Set font size
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 18}
plt.rc('font', **font)

fig, ax = plt.subplots(2,1,figsize=(8, 10))

fnames = ['Tc.csv','Tm.csv']
data_type = ['Clearing','Melting']
anions = ['Br$^−$', 'PF6$^−$', 'BF4$^−$','N(CN)$_2^−$']
x = np.arange(len(anions))
axno = 0
width = 0.25

for fname in fnames:
    
    data = pd.read_csv(fname)
    labels = data.keys()[1:]

    for i in range(3):
        values = pd.to_numeric(data.iloc[:4,i+1]).values
        ax[axno].bar(x+width*(i-1),values,width,label=labels[i])
    
    ax[axno].set_ylabel(f"{data_type[axno]} Temperature / °C")
    
    axno += 1

ax[0].set_xticks([],[])
ax[1].set_xticks(x,anions)
ax[1].set_xlabel('Anion')
ax[1].legend(loc=(0.45,0.85))
plt.savefig('multiplot.png',bbox_inches='tight',dpi=500)

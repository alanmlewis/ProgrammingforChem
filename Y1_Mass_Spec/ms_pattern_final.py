# This Python script will produce the isotope pattern seen in a
# a mass spectrum for the molecule or fragment formula provided

# ----- LOAD LIBRARIES --------------------------------------------------------------
from isotope_data import data
import numpy as np
from scipy.stats import multinomial
from functools import reduce

# ----- INPUT OPTIONS --------------------------------------------------------------
mol = 'C3H7NO2S' # Molecule / Fragment formula
fname = 'isotope_pattern' # The name of the .png and .csv output files
resolution = 0 # Number of decimal places for the mass (Choose 0 for quadrapole, choose 3 for ToF)
threshold = 1e-6 # Probability threshold at which element combinations are discarded

print(f'Drawing an isotope pattern for {mol}')

# ----- COUNT ATOMS IN MOLECULE ----------------------------------------------------
# This section collects together the number of each type of atom in the formula
# You should not edit this section
atoms = {}
i = 0 
while i < len(mol):
    if i==len(mol)-1:
        element = mol[i]
    elif mol[i+1].islower():
        element = mol[i:i+2]
        i += 1
    else:
        element = mol[i]
    if element not in atoms.keys():
        atoms[element] = 0
    if i==len(mol)-1:
        atoms[element] += 1
    elif mol[i+1].isdigit():
        j = 1
        while i+j < len(mol) and not mol[i+j].isupper(): j += 1
        atoms[element] += int(mol[i+1:i+j])
        i += j-1
    else:
        atoms[element] += 1
    i += 1

# ----- CALCULATE MULTINOMIAL PROBABILITIES ------------------------------------------
# This section works out the intensity of the peaks seen in the mass spectrum for every
# possible isotopologue. This uses the scipy function multinomial.
# You should not edit this section
def seqs(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in seqs(length - 1, total_sum - value):
                yield permutation + (value,) 

prob = []
mass = []
i = 0
for atom,number in atoms.items():
    prob.append([])
    mass.append([])
    atom_data = np.array(data[atom])
    atom_data = atom_data[atom_data[:,1].argsort()[::-1]]
    atom_data[:,1] *= 0.01
    dist = multinomial(number,atom_data[:,1])
    n_iso = len(atom_data)
    combis = seqs(n_iso,number)
    for comb in combis:
        comb_prob = dist.pmf(comb)
        if comb_prob < threshold: continue
        prob[i].append(comb_prob)
        mass[i].append(np.dot(comb,atom_data[:,0]))
        
    i += 1

mass_result = np.array(reduce(np.add.outer,mass)).reshape(-1)
prob_result = np.array(reduce(np.multiply.outer,prob)).reshape(-1)
mask = prob_result > threshold
mass_result = mass_result[mask]
prob_result = prob_result[mask]
idx = mass_result.argsort()
mass_result = mass_result[idx]
prob_result = prob_result[idx]
print('Fraction of spectrum discarded = ',1-np.sum(prob_result))

# ----- CALCULATE MULTINOMIAL PROBABILITIES ------------------------------------------
# Collect together peaks which are not distinguishable at the given resolution
low_res_mass = []
low_res_prob = []
for i,mass in enumerate(mass_result):
    lr_mass = np.round(mass,resolution)
    if lr_mass in low_res_mass:
        low_res_prob[-1] += prob_result[i]
    else:
        low_res_mass.append(lr_mass)
        low_res_prob.append(prob_result[i])

# ----- DATA MANIPULATION --------------------------------------------------------------
x = np.array(low_res_mass)
y = np.array(low_res_prob)
y = y/np.max(y)*100

# ----- PLOTTING DETAILS ---------------------------------------------------------------
import matplotlib.pyplot as plt

# Create a 'stem' plot with vertical lines up to the intensity value, with an x symbol at the top
plt.stem(x,y,markerfmt='x')

# Label each vertical line with its x coordinate
for i,j in zip(x,y):
    plt.annotate(str(i),xy=(i,j))

# Add a label showing which formula the spectrum is for
plt.text(0.6,0.9,f'Isotope Pattern for {mol}',transform=plt.gca().transAxes)
# Label the x and y axis
plt.xlabel('M/Z ')
plt.ylabel('Relative intensity')
# Save the spectrum
plt.savefig(f'{fname}.png')

# Save the raw data for the spectrum
frmt = '%.'+str(resolution)+'f,%.6e'
np.savetxt(f'{fname}.csv',np.vstack([np.round(x,resolution),y]).T,fmt=frmt)

print(f'Spectrum drawn sucessfully!')

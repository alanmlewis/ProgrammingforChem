# This Python script will list the molecules which could produce an M+ peak
# at the mass provided, taking into account the resolution provided.

# ----- LOAD LIBRARIES --------------------------------------------------------------
from isotope_data import data
import numpy as np
from sys import argv

# ----- DETERMINE RESOLUTION --------------------------------------------------------
try:
    idx = argv[1].index('.') # Find the position of the decimal
    x_resolution = len(argv[1]) - idx - 1 # Calculate the number of positions after the decimal
except:
	x_resolution = 0 # If there is no decimal, assume it is an integer
total_mass = float(argv[1]) # Convert the mass to a number
if x_resolution == 0: total_mass = int(total_mass) # Convert the mass to an integer if no decimal places provided
print(f'Finding possible chemical formulae which could have total weight {total_mass}')

# ----- SET UP LISTS --------------------------------------------------------
possible_molecules = [] # Create an empty list to contain all possible molcules
elements = list(data.keys()) # Create a list of every element in our data dictionary
numbers = np.zeros(len(elements),dtype=int) # Create a list of the number of each element in the formula. We begin with all equal to 0.
i = 0 
n = len(elements)

def get_formula(data,mass,i):
	# This is a recursive function which evaluates all possible formulae which produce a mass which could be close to the target mass
    if i == n: return # Exit the loop once we have gone through every element
    el = elements[i] # Get the current element
    min_mass = data[el][0][0] # Get the lowest isotopic mass of that element
    n_i = int((mass+ 10**-x_resolution/2) // min_mass ) # Calculate the maximum number of atoms of this element which could 'fit' into this mass
    numbers[i] = n_i # Update the number of atoms of this element in the formula
    # If the current combination of elements matches the mass, add the formula to the list of possibilities
    if round(n_i*min_mass-mass,x_resolution) == 0.0: 
        frag = ''
        for j,el in enumerate(elements):
           if numbers[j] == None or numbers[j] <= 0: continue
           if numbers[j] > 1:
               frag += el+str(numbers[j])
           else:
               frag += el
        if frag not in possible_molecules: possible_molecules.append(frag)
    # For each possible number of atoms of this element, loop over all other elements
    for j in range(n_i,-1,-1):
        get_formula(data,mass-n_i*min_mass,i+1)
        n_i -= 1
        numbers[i] = n_i

# Call the recursive function
get_formula(data,total_mass,i)

# If we only found one possible match, we've identified the molecule
if len(possible_molecules) == 1:
	print('Molecule identified as: ',possible_molecules[0])
# If we found nothing, something has gone wrong
elif len(possible_molecules) == 0:
    print(f"This weight doesn't match any possible molecules made from {elements} at this resolution. Try rounding to a lower resolution, or add more elements to your data dictionary.")
# If we have multiple possible molecules, we need to use more information to work out which is likely.
else:
	print(f"All of the following molecular formulae have mass {total_mass} to {x_resolution} decimal places:")
	for mol in possible_molecules:
		print(mol)

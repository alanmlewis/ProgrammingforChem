from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs
from ase.io import read
import numpy as np
import pandas as pd

# Select suitable data from dataset

nBits = 2048
fpgen = AllChem.GetMorganGenerator(radius=2,fpSize=nBits)
suppl = Chem.SDMolSupplier('pKa_QR.sdf')

# Get values out of dataset, and generate fingerprints
xyz_mols = []
names = []
pkas = []
fingerprint = []
for mol in suppl:
    try:
        if len(mol.GetAtoms())>30: continue
        xyz_mols.append(Chem.rdmolfiles.MolToXYZBlock(mol))
    except:
        continue
    names.append(mol.GetProp("Substance_Name"))
    pkas.append(mol.GetProp("pKa_b"))
    a = np.zeros(nBits)
    DataStructs.ConvertToNumpyArray(fpgen.GetFingerprint(mol),a)
    fingerprint.append(a)

names = ['NoName' if x=='' else x for x in names]
print(f"# Readable structures in dataset: {len(names)}")

# Remove NaN values from the dataset
pkas = pd.Series(pkas)
pkas = pkas.replace('NAN',np.nan).astype(float).to_numpy()
idx = np.where(1-pd.isnull(pkas))[0]

fingerprint = np.array(fingerprint)
fingerprint = fingerprint[idx]
pkas = pkas[idx]
names = [names[i] for i in idx]

print(f"# Structures after excluding NaN pka values: {len(names)}")

np.savetxt('fingerprints.txt',fingerprint,fmt='%i')
np.savetxt('pkas.txt',pkas,fmt='%.2f')
f = open('structures.xyz', 'w')
g = open('names.txt','w')
n = len(idx)
for i in idx:
        f.write(f"{xyz_mols[i]}")
for name in names:
        g.write(f"{name}\n")
        
f.close()
g.close()


# Limit elements at O
structures = read('structures.xyz',":")
idx = []
for i in range(n):
  numbers = structures[i].get_atomic_numbers()
  if sorted(set(numbers))[-1] <= 8: idx.append(i)

fingerprint = fingerprint[idx]
pkas = pkas[idx]
names = [names[i] for i in idx]
print(f"# Structures after excluding atoms > O: {len(names)}")

# Remove extreme pka Values
idx = np.where((pkas > 0) & (pkas < 15))[0]
names = [names[i] for i in idx]
fingerprint = fingerprint[idx]
pkas = pkas[idx]
print(f"# Structures after excluding extreme pkas: {len(names)}")

np.savetxt('fingerprints_selected.txt',fingerprint,fmt='%i')
np.savetxt('pkas_selected.txt',pkas,fmt='%.2f')
g = open('names_selected.txt','w')
for name in names:
        g.write(f"{name}\n")

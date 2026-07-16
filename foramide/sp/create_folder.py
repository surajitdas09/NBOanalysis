from glob import glob
import os 

dihedrals = sorted(glob('../dihedrals/*xyz'))

for dihedral in dihedrals:
    os.system(f'mkdir {dihedral[-16:-4]}')
    os.system(f'cp {dihedral} {dihedral[-16:-4]}/dihedral.xyz')


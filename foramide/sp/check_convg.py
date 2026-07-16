from glob import glob
  
dihedrals = [10*ang for ang in range(19)]

for dihedral in dihedrals:
    with open(f'dihedral_{dihedral:03d}/sp.out','r') as file:
        lines = file.readlines()
    file.close()

    print(lines[-2].strip())


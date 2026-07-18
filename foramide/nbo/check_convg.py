from glob import glob
  
dihedrals = [10*ang for ang in range(10)]

for dihedral in dihedrals:
    with open(f'dihedral_{dihedral:03d}/nbo.out','r') as file:
        lines = file.readlines()
    file.close()

    print(lines[-2].strip())


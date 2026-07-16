from glob import glob

dihedrals = [10*ang for ang in range(19)]

for dihedral in dihedrals:
    with open(f'dihedral_{dihedral:03d}/sp.com','w') as file:

        file.write('! B3LYP cc-pVDZ def2/J RIJCOSX SP\n')
        file.write('\n')
        file.write('* xyzfile 0 1 dihedral.xyz\n')

    file.close()

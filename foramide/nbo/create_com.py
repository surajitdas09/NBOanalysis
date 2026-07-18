from glob import glob

dihedrals = [10*ang for ang in range(10)]

for dihedral in dihedrals:
    with open(f'dihedral_{dihedral:03d}/nbo.com','w') as file:

        file.write('! B3LYP cc-pVDZ def2/J RIJCOSX NBO\n')
        file.write('\n')
        file.write('* xyzfile 0 1 dihedral.xyz\n')

    file.close()

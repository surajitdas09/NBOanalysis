from ase.io import read,write

mol = read('../opt/opt.xyz')

dihedrals = [10*ang for ang in range(19)]

for dihedral in dihedrals:

    dihedral_1024 = mol.get_dihedral(1,0,2,4)
    dihedral_1025 = mol.get_dihedral(1,0,2,5)

    new_mol = mol.copy()

    new_mol.set_dihedral(1,0,2,4,dihedral_1024+dihedral)
    new_mol.set_dihedral(1,0,2,5,dihedral_1025+dihedral)
    
    write(f"dihedral_{dihedral:03d}.xyz", new_mol)
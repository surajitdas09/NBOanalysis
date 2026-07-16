for f in dihedral_*; do
  echo $f
  cd $f
  runorca ${f}_sp qa 14 sp.com   min 6.0.1
  cd ..
done

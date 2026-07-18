for f in dihedral_*; do
  echo $f
  cd $f
  runorca ${f}_nbo qa 14 nbo.com all 6.0.1
  cd ..
done

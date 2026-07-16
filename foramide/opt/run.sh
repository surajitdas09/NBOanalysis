#!/bin/bash
#PBS -V
#PBS -N opt
#PBS -q workq
#PBS -l nodes=1:ncpus=18
export OMP_NUM_THREADS=1
ulimit -s unlimited
export PATH=/apps/openmpi/openmpi-3.1.3_install/bin:$PATH
export LD_LIBRARY_PATH=/apps/openmpi/openmpi-3.1.3_install/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/apps/lib:$LD_LIBRARY_PATH
WORKDIR=/scratch/surajit/PBS_$PBS_JOBID
mkdir $WORKDIR
cd $WORKDIR
ORCA=/apps/orca/orca.6.0.1/orca
export QCSCRATCH=$WORKDIR
mydir=/home/surajit/nbo_analysis/formamide/opt
cp $mydir/* .
echo $HOSTNAME > scrpath.txt
echo $PWD >> scrpath.txt
cp scrpath.txt $mydir/
$ORCA opt.com > opt.out
cp *.out *xyz $mydir/
rm -rf $WORKDIR

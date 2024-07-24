#!/bin/bash
#cd $SLURM_SUBMIT_DIR
pushd ~/bSub_runMe

for F in imerg_download_*.bash ; do
  sbatch -e ~/bSub_logMe/%j.error -o ~/bSub_logMe/%j.out < $F
  mv $F ~/bSub_doneMe/
done

popd



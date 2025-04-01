#!/bin/bash
#cd $SLURM_SUBMIT_DIR
pushd ~/bSub_runMe

#simulation=(47 51 73)

#for i in "${simulation[@]}"
for i in {0..30}
do
  #  echo $i
  sbatch -e ~/bSub_logMe/%j.error -o ~/bSub_logMe/%j.out TAsto_IM_sim_$i.bash
  mv TAsto_IM_sim_$i.bash ~/bSub_doneMe/
  
done
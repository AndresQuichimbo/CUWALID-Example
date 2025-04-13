#!/bin/bash
#cd $SLURM_SUBMIT_DIR
pushd ~/bSub_runMe

#sbatch -e ~/bSub_logMe/%j.error -o ~/bSub_logMe/%j.out HAD_gh_GHsim_0.bash
#  mv HAD_gh_GHsim_0.bash ~/bSub_doneMe/

#sbatch -e ~/bSub_logMe/%j.error -o ~/bSub_logMe/%j.out HAD_gh_IMsim_0.bash
#  mv HAD_gh_IMsim_0.bash ~/bSub_doneMe/

#sbatch -e ~/bSub_logMe/%j.error -o ~/bSub_logMe/%j.out /user/home/km19051/bSub_runMe/KE_IM_sim_0.bash
#  mv HAD_gh_GHsim_0.bash ~/bSub_doneMe/

#sbatch -e ~/bSub_logMe/%j.error -o ~/bSub_logMe/%j.out HAD_IM_sim_lon_0.bash
#  mv HAD_IM_sim_lon_0.bash ~/bSub_doneMe/

#sbatch -e ~/bSub_logMe/%j.error -o ~/bSub_logMe/%j.out /user/home/km19051/bSub_runMe/HAD_IM_sim_lon_0.bash
#  mv /user/home/km19051/bSub_runMe/HAD_IM_sim_lon_0.bash ~/bSub_doneMe/

#sbatch -e ~/bSub_logMe/%j.error -o ~/bSub_logMe/%j.out /user/home/km19051/KE_IM_sim.bash
#  mv /user/home/km19051/KE_IM_sim.bash ~/bSub_doneMe/

#sbatch -e ~/bSub_logMe/%j.error -o ~/bSub_logMe/%j.out /user/home/km19051/bSub_runMe/HAD_basin_IM_sim.bash
#  mv /user/home/km19051/bSub_runMe/HAD_basin_IM_sim.bash ~/bSub_doneMe/

sbatch -e ~/bSub_logMe/%j.error -o ~/bSub_logMe/%j.out /user/home/km19051/bSub_runMe/TAa_IM_sim.bash
#  mv /user/home/km19051/bSub_runMe/TA_IM_sim.bash ~/bSub_doneMe/

#sbatch -e ~/bSub_logMe/%j.error -o ~/bSub_logMe/%j.out /user/home/km19051/bSub_runMe/JUa_IM_sim.bash
#  mv /user/home/km19051/bSub_runMe/JU_IM_sim.bash ~/bSub_doneMe/

#sbatch -e ~/bSub_logMe/%j.error -o ~/bSub_logMe/%j.out /user/home/km19051/bSub_runMe/SHa_IM_sim.bash
#  mv /user/home/km19051/bSub_runMe/SH_IM_sim.bash ~/bSub_doneMe/


#sbatch -e ~/bSub_logMe/%j.error -o ~/bSub_logMe/%j.out /user/home/km19051/bSub_runMe/HAD_IM_sim.bash
#  mv /user/home/km19051/bSub_runMe/HAD_IM_sim.bash ~/bSub_doneMe/
  
popd

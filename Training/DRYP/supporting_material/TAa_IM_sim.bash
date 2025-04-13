#!/bin/bash
#SBATCH --job-name=TA_sim_33
#SBATCH --time=1:30:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=80gb
#SBATCH --account=GEOG028724
#cd $SLURM_SUBMIT_DIR
cd /user/home/km19051/DRYPv2.0_test/ 
source /user/home/km19051/miniconda3/bin/activate 
python /user/home/km19051/DRYPv2.0_test/run_model_input.py /user/work/km19051/Tana/HAD_IMERGa_Tana_input_sim.dmp

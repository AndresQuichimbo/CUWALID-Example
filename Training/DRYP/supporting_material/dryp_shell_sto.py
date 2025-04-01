# This script prepare the .bash file containing the arguments for downloading data
import numpy as np

def write_bsub_imerg_basin(npar):
	run_file = '../bSub_runMe/SHa_IM_sim_' + str(npar) + '.bash'
	lines = []
	lines.append('#!/bin/bash'+'\n')
	lines.append('#SBATCH --job-name=' + 'SH_sim_'+str(npar)+'\n')
	lines.append('#SBATCH --time=0:40:00'+'\n')
	lines.append('#SBATCH --nodes=1'+'\n')
	lines.append('#SBATCH --ntasks-per-node=1'+'\n')
	lines.append('#SBATCH --mem=80gb'+'\n')
	lines.append('#SBATCH --account=GEOG028724'+'\n')
	lines.append('#cd $SLURM_SUBMIT_DIR'+'\n')
	lines.append('cd /user/home/km19051/DRYPv2.0/'+' '+'\n')
	#lines.append('#module load lang/python/anaconda/3.9.7-2021.12-tensorflow.2.7.0'+' '+'\n')
	#lines.append('source /user/home/km19051/dryp/bin/activate'+' '+'\n')
	lines.append('source /user/home/km19051/miniconda3/bin/activate'+' '+'\n')
	lines.append('python /user/home/km19051/DRYPv2.0/run_model_input.py /user/work/km19051/Shabelle/HAD_IMERGa_Shabelle_input_sim_'+str(npar)+'.dmp' + '\n')
	
	f = open(run_file, 'w')
	for line in lines:
		f.write(line)
	f.close()
	return 'done'

def write_bsub_imerg_basin_TA(npar):
	run_file = '../bSub_runMe/TAsto_IM_sim_' + str(npar) + '.bash'
	lines = []
	lines.append('#!/bin/bash'+'\n')
	lines.append('#SBATCH --job-name=' + 'TA_sim_'+str(npar)+'\n')
	lines.append('#SBATCH --time=0:10:00'+'\n')
	lines.append('#SBATCH --nodes=1'+'\n')
	lines.append('#SBATCH --ntasks-per-node=1'+'\n')
	lines.append('#SBATCH --mem=80gb'+'\n')
	lines.append('#SBATCH --account=GEOG028724'+'\n')
	lines.append('#cd $SLURM_SUBMIT_DIR'+'\n')
	lines.append('cd /user/home/km19051/DRYPv2.0/'+' '+'\n')
	#lines.append('#module load lang/python/anaconda/3.9.7-2021.12-tensorflow.2.7.0'+' '+'\n')
	#lines.append('source /user/home/km19051/dryp/bin/activate'+' '+'\n')
	lines.append('source /user/home/km19051/miniconda3/bin/activate'+' '+'\n')
	lines.append('python /user/home/km19051/DRYPv2.0/run_model_input.py /user/work/km19051/Tana/HAD_IMERGa_Tana_input_forecasting_'+str(npar)+'.dmp' + '\n')
	
	f = open(run_file, 'w')
	for line in lines:
		f.write(line)
	f.close()
	return 'done'
	
def write_bsub_imerg_basin_JU(npar):
	run_file = '../bSub_runMe/JUsto_IM_sim_' + str(npar) + '.bash'
	lines = []
	lines.append('#!/bin/bash'+'\n')
	lines.append('#SBATCH --job-name=' + 'JU_sim_'+str(npar)+'\n')
	lines.append('#SBATCH --time=0:40:00'+'\n')
	lines.append('#SBATCH --nodes=1'+'\n')
	lines.append('#SBATCH --ntasks-per-node=1'+'\n')
	lines.append('#SBATCH --mem=80gb'+'\n')
	lines.append('#SBATCH --account=GEOG028724'+'\n')
	lines.append('#cd $SLURM_SUBMIT_DIR'+'\n')
	lines.append('cd /user/home/km19051/DRYPv2.0/'+' '+'\n')
	#lines.append('#module load lang/python/anaconda/3.9.7-2021.12-tensorflow.2.7.0'+' '+'\n')
	#lines.append('source /user/home/km19051/dryp/bin/activate'+' '+'\n')
	lines.append('source /user/home/km19051/miniconda3/bin/activate'+' '+'\n')
	lines.append('python /user/home/km19051/DRYPv2.0/run_model_input.py /user/work/km19051/Juba/HAD_IMERGa_Juba_input_sim_'+str(npar)+'.dmp' + '\n')

	f = open(run_file, 'w')
	for line in lines:
		f.write(line)
	f.close()
	return 'done'


if __name__ == '__main__':	
	npars=np.arange(30)
	#for ipar in range(22,31):
	for ipar in npars:
		write_bsub_imerg_basin_TA(ipar)
		#write_bsub_imerg_basin_JU(ipar)






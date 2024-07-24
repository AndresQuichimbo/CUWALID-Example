# This script prepare the .bash file containing the arguments for downloading data
import numpy as np
def write_bsub(year):
    run_file = 'bSub_runMe/imerg_download_' + str(year) + '.bash'
    lines = []
    lines.append('#!/bin/bash'+'\n')
    lines.append('#SBATCH --job-name=i' + str(year) +'\n')
    lines.append('#SBATCH --time=24:00:00'+'\n')
    lines.append('#SBATCH --nodes=1'+'\n')
    lines.append('#SBATCH --ntasks-per-node=1'+'\n')
    lines.append('#SBATCH --mem=4gb'+'\n')
    lines.append('#SBATCH --account=geog014522'+'\n')
    lines.append('#cd $SLURM_SUBMIT_DIR'+'\n')
    lines.append('cd /user/home/fp20123/'+' '+'\n')
    lines.append('module add lang/python/anaconda/3.7-2019.10'+' '+'\n')
    lines.append('source /user/home/fp20123/my_uavproject/bin/activate'+' '+'\n')
    lines.append('python /user/home/fp20123/download_tamsat3.py ' + str(year) +'\n')

    f = open(run_file, 'w')
    for line in lines:
        f.write(line)
    f.close()
    return 'done'


def write_bsub_cdo_cat(year):
    run_file = 'bSub_runMe/imerg_cat_' + str(year) + '.bash'
    lines = []
    lines.append('#!/bin/bash'+'\n')
    lines.append('#SBATCH --job-name=i' + str(year) +'\n')
    lines.append('#SBATCH --time=1:00:00'+'\n')
    lines.append('#SBATCH --nodes=1'+'\n')
    lines.append('#SBATCH --ntasks-per-node=1'+'\n')
    lines.append('#SBATCH --mem=10gb'+'\n')
    lines.append('#SBATCH --account=geog014522'+'\n')
    lines.append('#cd $SLURM_SUBMIT_DIR'+'\n')
    lines.append('cd /user/home/fp20123/'+' '+'\n')
    lines.append('module add lang/python/anaconda/3.7-2019.10'+' '+'\n')
    lines.append('source /user/home/fp20123/my_uavproject/bin/activate'+' '+'\n')
    lines.append('python /user/home/fp20123/cdo_mergetime.py ' + str(year) +'\n')

    f = open(run_file, 'w')
    for line in lines:
        f.write(line)
    f.close()
    return 'done'    
    
def write_bsub_threshold(pval, year):
    run_file = 'bSub_runMe/imerg_perc_' + str(year) + '.bash'
    lines = []
    lines.append('#!/bin/bash'+'\n')
    lines.append('#SBATCH --job-name=i' + str(year) +'\n')
    lines.append('#SBATCH --time=0:15:00'+'\n')
    lines.append('#SBATCH --nodes=1'+'\n')
    lines.append('#SBATCH --ntasks-per-node=1'+'\n')
    lines.append('#SBATCH --mem=120gb'+'\n')
    lines.append('#SBATCH --account=geog014522'+'\n')
    lines.append('#cd $SLURM_SUBMIT_DIR'+'\n')
    lines.append('cd /user/home/fp20123/'+' '+'\n')
    lines.append('module add lang/python/anaconda/3.7-2019.10'+' '+'\n')
    lines.append('source /user/home/fp20123/my_uavproject/bin/activate'+' '+'\n')
    lines.append('python /user/home/fp20123/aridity_africa/av_crit_analysis_imerg.py 95 ' + str(year) +'\n')

    f = open(run_file, 'w')
    for line in lines:
        f.write(line)
    f.close()
    return 'done'    

def write_bsub_threshold_all(pval, ind):
    run_file = 'bSub_runMe/chirps_perc_' + str(pval) + '.bash'
    lines = []
    lines.append('#!/bin/bash'+'\n')
    lines.append('#SBATCH --job-name=i' + str(pval) +'\n')
    lines.append('#SBATCH --time=2:30:00'+'\n')
    lines.append('#SBATCH --nodes=1'+'\n')
    lines.append('#SBATCH --ntasks-per-node=1'+'\n')
    lines.append('#SBATCH --mem=30gb'+'\n')
    lines.append('#SBATCH --account=geog014522'+'\n')
    lines.append('#cd $SLURM_SUBMIT_DIR'+'\n')
    lines.append('cd /user/home/fp20123/'+' '+'\n')
    lines.append('module add lang/python/anaconda/3.7-2019.10'+' '+'\n')
    lines.append('source /user/home/fp20123/my_uavproject/bin/activate'+' '+'\n')
    lines.append('python /user/home/fp20123/aridity_africa/ai_change_africa.py ' + str(pval) +'\n')

    f = open(run_file, 'w')
    for line in lines:
        f.write(line)
    f.close()
    return 'done'    
    

def write_bsub_trend_chirps(pval, ind):
    run_file = 'bSub_runMe/chirps_' + str(ind) +'_'+ str(pval) + '.bash'
    lines = []
    lines.append('#!/bin/bash'+'\n')
    lines.append('#SBATCH --job-name=i_' + str(ind) +'_'+ str(pval) +'\n')
    lines.append('#SBATCH --time=0:30:00'+'\n')
    lines.append('#SBATCH --nodes=1'+'\n')
    lines.append('#SBATCH --ntasks-per-node=1'+'\n')
    lines.append('#SBATCH --mem=30gb'+'\n')
    lines.append('#SBATCH --account=geog014522'+'\n')
    lines.append('#cd $SLURM_SUBMIT_DIR'+'\n')
    lines.append('cd /user/home/fp20123/'+' '+'\n')
    lines.append('module add lang/python/anaconda/3.7-2019.10'+' '+'\n')
    lines.append('source /user/home/fp20123/my_uavproject/bin/activate'+' '+'\n')
    lines.append('python /user/home/fp20123/aridity_africa/ai_change_africa.py ' + str(ind) +' '+ str(pval) +'\n')

    f = open(run_file, 'w')
    for line in lines:
        f.write(line)
    f.close()
    return 'done'    
    
    
if __name__ == '__main__':
  inds=np.arange(1,5)
  pvals = [95,99]
  for i in range(0,len(inds)):
    ind=inds[i]
#    pval = pvals[i]
##    write_bsub_cdo_cat(year)
    write_bsub_trend_chirps(95, ind)
    write_bsub_trend_chirps(99, ind)
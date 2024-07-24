import os
import numpy as np
import pandas as pd

def write_sim_file(fname_input, newfname_input, parameter):
	""" modify the parematers of the model input file and
		model setting file.
		WARNING: it will reeplace the original file, so
		make a copy of the original files
	parameters:
		filename_input:	model inputfile, including path
		parameter:		1D array of model paramters
	"""
	
	# Check if input file exist
	if not os.path.exists(fname_input):
		raise ValueError("File not availble")
	
	# simulation number
	sim = str(int(parameter[0]))
	
	# Read model input file
	f = pd.read_csv(fname_input)
	
	# Change model name by adding the simulation number
	f.drylandmodel[1] = f.drylandmodel[1] + sim

	# change parameters of the of the setting parameter file
	fname_settings = f.drylandmodel[87]
	# create a copy of the file with the new name
	fname_root = fname_settings.split('.')[0]
	fname_ext = fname_settings.split('.')[1]
	# new input file name
	newfname_settings = fname_root+'_'+sim+'.'+fname_ext
	#copyfile(fname_settings, newfname_settings)
	# replace new setting file
	f.drylandmodel[87] = newfname_settings
	# Open setting parameter file
	fsimpar = pd.read_csv(fname_settings)	
	
	# Change setting parameter file with new values
	fsimpar['DWAPM_SET'][46] = ('%.5f' % parameter[1]) # kdt
	fsimpar['DWAPM_SET'][48] = ('%.5f' % parameter[2]) # kDroot
	fsimpar['DWAPM_SET'][50] = ('%.2f' % parameter[3]) # kAWC
	fsimpar['DWAPM_SET'][52] = ('%.5f' % parameter[4]) # kKsat
	fsimpar['DWAPM_SET'][54] = ('%.5f' % parameter[5]) # kSigma
	fsimpar['DWAPM_SET'][56] = ('%.5f' % parameter[6]) # kKch
	fsimpar['DWAPM_SET'][58] = ('%.5f' % parameter[7]) # T
	fsimpar['DWAPM_SET'][60] = ('%.5f' % parameter[8]) # kW
	fsimpar['DWAPM_SET'][62] = ('%.5f' % parameter[9]) # kKaq
	fsimpar['DWAPM_SET'][64] = ('%.5f' % parameter[10])# kSy
	
	# Reeplace model input and parameters file
	os.remove(newfname_input) if os.path.exists(newfname_input) else None
	os.remove(newfname_settings) if os.path.exists(newfname_settings) else None
	
	# Write model parameter and input file
	f.to_csv(newfname_input, index=False)
	fsimpar.to_csv(newfname_settings, index=False)

#filename_paramerer = '../Kenya/KE_parameter_set_MSWEP.csv'
def gen_array_input_files(fname_input):
	#fname_paramerer_sets = "/user/work/km19051/Kenya_data/EW_par_set_ch_GIRHAF.csv"
	fname_paramerer_sets = "/user/work/km19051/basin_data/HAD_par_set_ch_GIRHAF_cal.csv"
	parameter = pd.read_csv(fname_paramerer_sets)
	
	#Create a copy of inputfile
	fname_root = fname_input.split('.')[0]
	fname_ext = fname_input.split('.')[1]
	for npar in range(0, 100):
		# new input file name
		newfname_input = fname_root+'_'+str(npar)+'.'+fname_ext
		# create a new input file
		#copyfile(fname_input, newfname_input)
		# replace all new values in dataset
		write_sim_file(fname_input, newfname_input, parameter.loc[npar])

# ========================================================
# LOOP FOR CREATING MULTIPLE IMPOT FILES FOR RUNNING IN HPC
fname = [
#'/user/work/km19051/Kenya/MCch/IMERG/EW_D2E_IM_chd_sim.dmp',
#'/user/work/km19051/Kenya/MCch/GIRHAF/EW_D2E_GH_chd_sim.dmp',
'/user/work/km19051/Shabelle/HAD_IMERGcal_Shabelle_input_sim.dmp',
'/user/work/km19051/Juba/HAD_IMERGcal_Juba_input_sim.dmp',
'/user/work/km19051/Tana/HAD_IMERGcal_Tana_input_sim.dmp',
]

for ifname in fname:
	gen_array_input_files(ifname)
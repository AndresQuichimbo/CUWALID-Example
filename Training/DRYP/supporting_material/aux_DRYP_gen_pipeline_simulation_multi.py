import os
import numpy as np
import pandas as pd

def write_sim_file_pipeline(fname_input, newfname_input,
	sim_ini='1999', sim_end='2000',
	date_ini='2000 1 1', date_end='2001 1 1',
	save_settings=True, save_riparian=True):
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
	
	#date_ini = 
	#date_end = str
	
	# simulation number
	#sim = str(int(parameter[0]))
	
	# Read model input file
	f = pd.read_csv(fname_input)
	
	# copy input file
	fnew = f.copy()
	# INPUT FILES ====================================
	# Change model name by adding the simulation number
	fnew.drylandmodel[1] = f.drylandmodel[1]+"_"+ sim_end
	
	# name and directory of previous time steps
	mname = f.drylandmodel[1] + "_"+sim_ini
	DirOutput = f.drylandmodel[81]# + '_' + sim_ini
	
	# new name
	fnew.drylandmodel[6] = f.drylandmodel[1] + '_' + sim_ini
	
	# change initial conditions Qo
	fnew.drylandmodel[6] = DirOutput+'/'+mname+'_avg_Q_ini.asc'
	# change initial conditions soil moisture
	fnew.drylandmodel[46] = DirOutput+'/'+mname+'_avg_tht_ini.asc'
	# change initial condition water table
	fnew.drylandmodel[57] = DirOutput+'/'+mname+'_avg_wte_ini.asc'
	
	# RIPARIAN FILES ==================================
	# change files of the riparian file	
	fname_riparian = f.drylandmodel[93]
	# create a copy of the file with the new name
	fname_rootrp = fname_riparian.split('.')[0]
	fname_extrp = fname_riparian.split('.')[1]
	# new input file name
	newfname_riparian = fname_rootrp + '_' + sim_end + '.' + fname_extrp
	#newfname_riparian = fname_rootrp + '_' + mname + '.' + fname_extrp
	# change initial condition riparian area
	# change initial conditions riparian water content
	fsimrip = pd.read_csv(fname_riparian)
	fsimrip.RIPARIAN[19] = DirOutput+'/'+mname+'_avg_tht_rp_ini.asc'
	
	# write name of riparian file in the input file
	fnew.drylandmodel[93] = newfname_riparian
	
	# SETTING FILES ===================================
	# change parameters of the of the setting parameter file	
	fname_settings = f.drylandmodel[87]
	# create a copy of the file with the new name
	fname_root = fname_settings.split('.')[0]
	fname_ext = fname_settings.split('.')[1]
	# new input file name
	newfname_settings = fname_root + '_' + sim_end + '.' + fname_ext
	#copyfile(fname_settings, newfname_settings)
	# replace new setting file
	fnew.drylandmodel[87] = newfname_settings
	
	
	# Open setting parameter file
	fsimpar = pd.read_csv(fname_settings)	
	
	# Change starting point of the simulation
	fsimpar.DWAPM_SET[2] = date_ini
		
	# change final date of the simulaition
	fsimpar.DWAPM_SET[4] = date_end

	# Reeplace model input and parameters file
	os.remove(newfname_input) if os.path.exists(newfname_input) else None
	if save_riparian is True:
		os.remove(newfname_riparian) if os.path.exists(newfname_riparian) else None
	
	if save_settings is True:
		os.remove(newfname_settings) if os.path.exists(newfname_settings) else None
	
	# Write model parameter and input file
	fnew.to_csv(newfname_input, index=False)
	if save_riparian is True:
		fsimrip.to_csv(newfname_riparian, index=False)
	if save_settings is True:
		fsimpar.to_csv(newfname_settings, index=False)

def change_sim_file_name(fname_input, newfname_input, sim=2000):
	# Check if input file exist
	if not os.path.exists(fname_input):
		raise ValueError("File not availble")
	
	f = pd.read_csv(fname_input)
	f.drylandmodel[1] = f.drylandmodel[1] + "_" + str(sim)
	# Reeplace model input and parameters file
	os.remove(newfname_input) if os.path.exists(newfname_input) else None
	# Write model parameter and input file
	f.to_csv(newfname_input, index=False)

def gen_inital_end_simulation_dates(year, month, day, dtyear=1, dtmonth=0, dtday=0):
	"""This function gets the initial and end date of a specified period
	"""
	date_ini = str(year+dtyear) + ' ' + str(month+dtmonth) + ' ' + str(day+dtday)
	date_end = str(year+dtyear+1) + ' ' + str(month+dtmonth) + ' ' + str(day+dtday)
	
	name = str(year)
	name_end = str(year+dtyear)
	
	return date_ini, date_end, name, name_end
# ========================================================
# LOOP FOR CREATING MULTIPLE IMPOT FILES FOR RUNNING IN HPC
fname = [
#'/user/work/km19051/Kenya/MCch/IMERG/EW_D2E_IM_chd_sim.dmp',
#'/user/work/km19051/Kenya/MCch/GIRHAF/EW_D2E_GH_chd_sim.dmp',
#"/user/work/km19051/HAD/HAD_IMERG_input_sim_28a.dmp",
#'/user/work/km19051/HAD/HAD_IMERG_input_sim.dmp'
#"/user/work/km19051/HAD/HAD_IMERG_input_sim_"+str(i)+".dmp" for i in range(31, 43)
"/user/work/km19051/HAD/HAD_IMERG_input_sim_"+str(i)+".dmp" for i in [72, 84]
]

#fname_input = "D:/test_folder/EW_D2E_IM_chd_sim_216.dmp"

# WARNINGS ----------------------------------------------------------------
# THIS FUNCTION ONLY GENERATE YEARLY FILES
# The initial file should specify the initial conditions at the begining of
# the simulation of the entire period, therefore, the name of inital model
# must be according to the name required to the next simulation
# subsequent periods will use the name files created with this function

# the inital file should be created with the model name without addig the year,
# basically, only the name of the model,  the year will be added automatically


for ifname_input in fname:
	newfname_input = ifname_input.split('.')[0]+'_2000.'+ifname_input.split('.')[1]
	change_sim_file_name(ifname_input, newfname_input)
	for iyear in range(2000, 2023):
		date_ini, date_end, name, name_end = gen_inital_end_simulation_dates(iyear, 1, 1)
		newfname_input = ifname_input.split('.')[0]+'_'+name_end+'.'+ifname_input.split('.')[1]
		write_sim_file_pipeline(ifname_input, newfname_input, sim_ini=name, sim_end=name_end,
			date_ini=date_ini, date_end=date_end
			)
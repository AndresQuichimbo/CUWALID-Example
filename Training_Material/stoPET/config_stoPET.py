# READ ME
#This config file is used to provide all the required 
# data and parameters to run the stoPET model and generate the 
# required seasonl forecasts accounting for the ICPAC temerature forecast
# given as a seasonal probability. 

# This will be used in both running the run_stoPET.py to generate multiple files
# of forecast pools with above, normal and below average forecasts.
# and finally use d in the forecast_generation.py for producing the final
# PET forecasts for the season accounting ICPAC temperature forecast.

## ----- CHANGE THE INPUT VARIABLES HERE -----##
# this is the data pathe where the stoPET parameter files are keept
datapath = '/home/adagmawi/CUWALID/CUWALID_training/stoPET/stopet_parameter_files/'

# this is the output path where you want to keep the generated PET files
outputpath = '/home/adagmawi/CUWALID/CUWALID_training/stoPET/result/'

# this is where you decide wherether to run a 'regional' model or 'single' point model
runtype =  'regional' 

# the number of years to generate data for
startyear = 2022
endyear = 2022
  
# this is the seasonal julian dates required as a start date and end date
seasonswitch = 1 
startdate = 60 
enddate = 151
seasonName = 'MAM'

# Single point stoPET run
latval = 1.0
lonval = 35.0

# Regional stoPET run (Kenya)
latval_min = -1.6
latval_max = 1.1
lonval_min = 35.9
lonval_max = 40.1 

# this is the number of ensembles you want to generate
number_ensm = 10

# this is the method you use for adjusting the PET to account for change in temperature
tempAdj = 2

# this is the change in temperature you prefer to have if you use tempAdj = 2
deltat = 0.0

# this is where you provide a sting of name to identify your region or point e.g. 'tana_basin'
locname = 'TanaBasin' 

# this is the user defined percentage change in PET if you use tempAdj = 1
udpi_pet = 5

# This is the file containing the ICPAC seasonal tercile temperature forecast.
# provide the full path where it is located
tercile_forecast_file = 'C:/Users/fp20123/Dropbox/CUWALID/new_stopet/TanaBasin_TempF_MAM2022.nc'     # Kenya

# This is especially important when deling with regions with coast.
# DRYP model require rew grid values to be available with data to 
# make boundary conditions. Hence we need to adthe ocean grids by filling 
# it with the neighbour land grid value. To do this first we need a proper
# mask file that make all the ocean grids to nan then we fill using xarray
# provide the full path where it is located
mask_file = 'C:/Users/fp20123/Dropbox/CUWALID/new_stopet/TanaBasin_mask.nc' 

  



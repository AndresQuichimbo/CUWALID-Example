import sys
import numpy as np
from stoPET_v1_4dryp import *

# READ ME
# In order to make the ensemble forecasts for running DRYP 
# here we produce the ensemble pools for the PET 
# to do this we need 3 pools one for each tercile (Above, Normal,Below)
# hence, we need to provide a locname variable with a standard system of ***_A (for above)
# ***_N (for normal) and ***_B(for below). the *** can be any name the user choose.
# the deltat should be (1.5 for above, 0.0 for normal and -1.5 for below)

# other changes can be made inside the run_stoPET() function 
def run_stoPET(locname, deltat):
    ## ----- CHANGE THE INPUT VARIABLES HERE -----##
    datapath = '/user/work/fp20123/stoPET/stopet_parameter_files/'
    outputpath = '/bp1/geog-tropical/data/ERA-Land/driving_data/HAD_PET_forecast/ens_1/'
    runtype =  'regional' # 'single'
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

    # Regional stoPET run
    latval_min = -7.0
    latval_max = 16.0
    lonval_min = 31.0
    lonval_max = 52.1 
    locname = locname 

    number_ensm = 30
    tempAdj = 2
    deltat = deltat
    udpi_pet = 5
    
    # This is specific for the forecast of PET using tercile forecasts 
    # this will allow to generate pool of above, below and normal PET forecasts
    # and the files will be stored in a folder with a specific nameing.
    if (tempAdj == 2) and (deltat > 0.):
      locname = locname + '_A' 
    elif (tempAdj == 2) and (deltat == 0.):
      locname = locname + '_N' 
    elif (tempAdj == 2) and (deltat < 0.):
      locname = locname + '_B'   
    else:
      locname = locname
    # these are smoothing function variables
    # it helps to smooth spatial vriability during randomization
    # smooother: uses 3 methods ('5Npoint', '9Npoint', 'Gaussian') and if you want no smoothing you can put 'none'
    # N: is the number of grid points from the center for Gaussian method only
    # npass: is the number of times the smoothing is done for the 5Npoint nad 9Npoint methods. 
    smoother =  '9Npoint'   # '5Npoint' '9Npoint' 'Gaussian' 'none'
    N = 3 
    npass = 2

    ## ------ NO CHANGES BELLOW THIS -------------##
    if seasonswitch == 0:
      if runtype == 'single':
            for ens_num in np.arange(0,number_ensm):
                    stoPET_wrapper_singlepoint(startyear, endyear, latval, lonval, locname,
                            ens_num,datapath, outputpath, tempAdj, deltat, udpi_pet)  #, seasonswitch, startdate, enddate
      elif runtype == 'regional':
            for ens_num in np.arange(0,number_ensm):
                    stoPET_wrapper_regional(startyear, endyear, latval_min, latval_max, lonval_min, lonval_max,
                            locname, ens_num, datapath, outputpath, tempAdj, deltat, udpi_pet, smoother, N, npass)
      else:
            raise ValueError('runtype only takes single and regional ... please check!')
    
    if seasonswitch == 1:
      if runtype == 'single':
            for ens_num in np.arange(0,number_ensm):
                    stoPET_wrapper_singlepoint(startyear, endyear, latval, lonval, locname,
                            ens_num,datapath, outputpath, tempAdj, deltat, udpi_pet)  #, seasonswitch, startdate, enddate
      elif runtype == 'regional':
            for ens_num in np.arange(0,number_ensm):
                    stoPET_wrapper_regional(startyear, endyear, latval_min, latval_max, lonval_min, lonval_max,
                            locname, ens_num, datapath, outputpath, tempAdj, deltat, udpi_pet, smoother, N, npass)
            # extract seasonal value and remove the annual files
            # prepare the files for the DRYP model input format
            # this only works for regional data as DRYP requires a catchment to run 
            seasonal_pet_for_dryp(outputpath, locname, number_ensm, tempAdj, startyear, endyear, startdate, enddate, seasonswitch)
      else:
            raise ValueError('runtype only takes single and regional ... please check!')
    
##-----------------------------------------------------------------------##
if __name__ == '__main__':
    start = dt.datetime.now()

    run_stoPET(str(sys.argv[1]),  float(sys.argv[2]))
    print('Seasonal PET extraction finished successfully.')
    
    end=dt.datetime.now()
    print('Time of run: %s'%(end - start))



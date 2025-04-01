import sys
import numpy as np
from stoPET_v1 import *

def run_stoPET():
    ## ----- CHANGE THE INPUT VARIABLES HERE -----##
    datapath = './stopet_parameter_files/'
    outputpath = './result/'
    runtype =   'regional' # 'single' 
    startyear = 1994
    endyear = 1996

    # Single point stoPET run
    latval = 3.8
    lonval = 36.6

    # Regional stoPET run
    latval_min = -5.5
    latval_max = -4.5 #5.5
    lonval_min = 33.0
    lonval_max = 34.5 #42.0
    locname = 'Kenya' #'Turkana1' #

    number_ensm = 2
    tempAdj = 3
    deltat = 1.5
    udpi_pet = 5

    ## ------ NO CHANGES BELLOW THIS -------------##
    if runtype == 'single':
            for ens_num in np.arange(0,number_ensm):
                    stoPET_wrapper_singlepoint(startyear, endyear, latval, lonval, locname,
                            ens_num,datapath, outputpath, tempAdj, deltat, udpi_pet)
    elif runtype == 'regional':
            for ens_num in np.arange(0,number_ensm):
                    stoPET_wrapper_regional(startyear, endyear, latval_min, latval_max, lonval_min, lonval_max,
                            locname, ens_num, datapath, outputpath, tempAdj, deltat, udpi_pet)
    else:
            raise ValueError('runtype only takes single and regional ... please check!')


##-----------------------------------------------------------------------##
if __name__ == '__main__':
    start = dt.datetime.now()

    run_stoPET()
    
    end=dt.datetime.now()
    print('Time of run: %s'%(end - start))



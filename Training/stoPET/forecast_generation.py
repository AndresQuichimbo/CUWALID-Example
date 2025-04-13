import numpy as np
import os
import sys
import datetime as dt
from netCDF4 import Dataset, num2date
from numba import jit, njit, prange
import xarray as xr
# this imports all the required parameters
from config_stoPET import *
# ===================================== #
# READ ME
# This script is prepared to generate the ensemble forecasts for PET
# based on the seasonal temperature forecast provided by ICPAC.
# Before runnig this script one should have prepared the forecast pools of PET
# by runing the stoPET model first. The number of ensembles provided  here 
# should be equal or less than what is available in each pool of stoPET forecast.

# changes can be made in the function forecast_wrapper()
# locname should be similar to what is provided while runing stoPET but only for one of the tercile categories
# for example if locname is TanaBasin then we should provide TanaBasin_A. the script will read this and extract the name from
# what is given. This is important to locate the ensemble files in each pool. 

# the other variables should be similar to the stoPET run exactly as they are used to name files.

def forecast_wrapper(tercile_forecast_file, outputpath, startyear, startdate, enddate, locname, number_ensm, tempAdj, seasonName, mask_file):  
  # this will reasd one file ffrom the stoPET output to use as a template for the array length and time
  nc = Dataset(outputpath + '%s_A_E0_StoPET/AdjstoPET_%s_%s_%s_%s.nc'%(locname, tempAdj, startdate, enddate, startyear))
  lats = nc.variables['latitude'][:]
  lons = nc.variables['longitude'][:]
  time = nc.variables['time']
  tunits = time.units
  ori_data = nc.variables['pet'][:,:,:]
  
  # create array to append data
  ens_f = (np.ones((number_ensm, ori_data.shape[0], ori_data.shape[1], ori_data.shape[2]))) * np.nan
  # this is just for now 
  # or_data is used to identify array shape so must be same as the origional
  # stopet generated data array for the season (time,lat,lon)
  nc = Dataset(tercile_forecast_file) 
  above = nc.variables['above'][:,:] 
  normal = nc.variables['normal'][:,:] 
  below = nc.variables['below'][:,:]  
  # tercile frorecast array
  tercileTf = np.asarray(np.stack([above,normal,below]))
  
  # Read the entire forecast loop as an array (ensemble, time, lat, lon)
  # This is required since the numba jit cant read files but only numpy array
  # Since we are reading all the files of pool it requre storage space
  ens_A, ens_N, ens_B = read_forecast_pool(number_ensm, ori_data, outputpath, locname, tempAdj, startdate, enddate, startyear)

  # loop through each grid and start extracting the respective timeseries 
  # make sure the number of files percentage is correct.
  # This means when you take 5% of 10 it is 0.5 this means we take 1 file for this category
  # this might reduce number of files for the other categories so make sure the sum is equal to 
  # total number of files we have (this is equal to the ensemble numbers).
  # run loop for selecting the forecast and write on a file
  
  # This is a parallel run using numba to redce computational time
  # but since we are reading all the files of pool it requre storage space
  ensembleArray = forecast_with_tercile(tercileTf, number_ensm, ens_A, ens_N, ens_B, ens_f)      
  
  # Write the output array into files                        
  writing_forecast_file(ensembleArray, seasonName, locname, startyear, outputpath, time, lats, lons, tunits, mask_file) 


def read_forecast_pool(number_ensm, ori_data, outputpath, locname, tempAdj, startdate, enddate, startyear):
    # create array to append data of each ensembles
    ens_A = (np.ones((number_ensm, ori_data.shape[0], ori_data.shape[1], ori_data.shape[2]))) * np.nan
    ens_N = (np.ones((number_ensm, ori_data.shape[0], ori_data.shape[1], ori_data.shape[2]))) * np.nan
    ens_B = (np.ones((number_ensm, ori_data.shape[0], ori_data.shape[1], ori_data.shape[2]))) * np.nan
    
    # file name of the adjusted PET from stopet
    fname = 'AdjstoPET_%s_%s_%s_%s.nc'%(tempAdj, startdate, enddate, startyear)
    # Above
    for ens in range(0,number_ensm):
        filepath = outputpath + locname + '_A_E%s_StoPET/'%ens
        # read the file and append to the 4D array
        nca = Dataset(filepath + fname)
        pet_A = nca.variables['pet'][:,:,:]
        ens_A[ens,:,:,:] = pet_A

    # Normal
    for ens in range(0,number_ensm):
        filepath = outputpath + locname + '_N_E%s_StoPET/'%ens
        # read the file and append to the 4D array
        ncn = Dataset(filepath + fname)
        pet_N = ncn.variables['pet'][:,:,:]
        ens_N[ens,:,:,:] = pet_N
        
    # Below
    for ens in range(0,number_ensm):
        filepath = outputpath + locname + '_B_E%s_StoPET/'%ens
        # read the file and append to the 4D array
        ncb = Dataset(filepath + fname)
        pet_B = ncb.variables['pet'][:,:,:]
        ens_B[ens,:,:,:] = pet_B
    
    return ens_A, ens_N, ens_B
    
     
# numba parallel run function  
# decorate the function  
@jit(nopython=True, parallel=True)  
def forecast_with_tercile(tercileTf, number_ensm, ens_A, ens_N, ens_B, ens_f):
    
    #loop through files and extract array of PET accordinglly  
    for i in prange(ens_f.shape[2]): # row # use parallel range
        for j in range(ens_f.shape[3]): # col
            # Here we need to put exceptions for the grids with empty seasonal forecast 
            # like the ocean area where there is no forecast. 
            # We do that by jumping the grid to save computationonal time.
            # all values will be -1 for those grids so easy to mask as thre are no negative PET in stoPET.
            if np.sum(tercileTf[:,i,j]) > 100.1:
                pass
            else:
                forcvals = tercileTf[:,i,j] * (number_ensm/100) # this is the forecast values
                # make sure the sum of the the above array is equal to the number of files
                # available. Here we need to make the floats rounded but still cant exceed
                # the numbe of file. 
                fnumbers = check_forecast_percentage(forcvals,number_ensm)
                choice_range = np.arange(number_ensm) # the array of numbers to choose from for random value

                start = 0 # this begin the start of the array 
                for v in range(0, len(fnumbers)):
                    inx = fnumbers[v]
                    # print('For: ',v, 'choice array is: ', choice_range, 'inx=',inx)
                    # randomly select numbers equal to inx
                    # the number selected should be less than 
                    # the number of files available. This will be
                    # used as ensemble value.
                    ensnum = np.random.choice(choice_range, size=int(inx), replace=False)
                    # once we get the ensembles we proceed to selecting the files
                    # extract the PET timeseries and add it to the empty array created above.
                    # ---------- new addition ------------
                    end = start + len(ensnum)
                    # this create array from which we decide to put the selected ensemble values
                    ensalloc = np.arange(start, end) 
                    # ------------------------------------
                    for e in range(0,len(ensnum)):
                        ens = int(ensnum[e])
                        ens_v = int(ensalloc[e])
                        if v == 0:
                            ens_f[ens_v,:,i,j] = ens_A[ens,:,i,j] 
                            #print(v,ens)
                        elif v == 1:
                            ens_f[ens_v,:,i,j] = ens_N[ens,:,i,j] 
                            #print(v,ens)
                        else:
                            ens_f[ens_v,:,i,j] = ens_B[ens,:,i,j] 
                            #print(v,ens)
                    # find the remain numbers that are not choosen to go for the next one.
                    # doing this avoids over writing of array.
                    choice_range=get_difference(choice_range,ensnum) 
                    #print('Final range: ', choice_range)
                    start = end # this updatesthe starting point to create array 
    return ens_f


@jit
def get_difference(choice_range,ensnum):
    choice_range_n = set(choice_range)
    ensnum_n = set(ensnum)
    return np.asarray(list(choice_range_n.difference(ensnum_n)))


@jit(nopython=True, parallel=True)          
def check_forecast_percentage(forcvals, num_file):  
  """
  This function evaluate the forecasts and the number of
  files we have and return the exact number of files we need to add 
  # for the three tercile category.
  """
  y = np.rint(np.nextafter(forcvals, forcvals+1))
  z=np.sum(y) - num_file
  if z!=0:
    ind = np.argmax(y)
    y[ind] = y[ind] - z  
  return y

 
def writing_forecast_file(ensembleArray, seasonName, locname, startyear, outputpath, time, lats, lons, tunits, mask_file): 
  # read mask
  nc = Dataset(mask_file) 
  mask = nc.variables['mask'][:,:]  
      
  # write the final ensembles on a netcdf file
  # create a folder to save the data
  if not os.path.isdir(outputpath + 'ensemble_forecast/'):
    os.mkdir(outputpath + 'ensemble_forecast/')
  # file name of the adjusted PET from stopet 
  for f in range(ensembleArray.shape[0]):
    # read the each ensemble array
    data = ensembleArray[f,:,:,:]
    # mask the oceans
    data = data * mask
    # Fill extra values using xarray.ffill and xarray.bfill
    # the limit values are specific to horn of Africa 
    # We always need to acess which fits best depeding on 
    # the shape of the costal region.
    # if the coast is veritcal ffill(f'dim_{2}') works
    # if it is horizontal bfill(f'dim_{1}' works
    # if it include both just make sure you find the right 
    # number of limits values. 
    # The best way to do this is to use cdo tool (cdo.setmisstonn)
    # this requires cdo tool and changing files. 
    data = xr.DataArray(data).bfill(f'dim_{1}', limit=8).values
    data = xr.DataArray(data).ffill(f'dim_{2}', limit=10).values
    # write the output files
    outpath = outputpath + 'ensemble_forecast/'
    filename = (outpath + 'Forecast_PET_%s_ens_%s_%s_%s.nc')%(locname,f,seasonName,startyear)
    varname = 'pet'
    timevals = time[:]
    forecast_nc_write(data, lats, lons, varname, timevals, tunits, filename)
  
  return None          

     
def forecast_nc_write(data, lat, lon, varname, timevals, tunits, filename):
    """
    this function write the PET on a netCDF file.

    :param: data: data to be written (time,lat,lon)
    :param: lat: latitude
    :param: lon: longitude
    :param: varname: name of the variable to be written (e.g. 'pet')
    :param: tunits: time units for the data (e.g. 'days since 1981-01-01')
    :param:filename: the file name to write the values with .nc extension

    :return:  produce a netCDF file in the same directory.
    """
    
    ds = Dataset(filename, mode='w', format='NETCDF4_CLASSIC')

    time = ds.createDimension('time', None)
    latitude = ds.createDimension('latitude', len(lat))
    longitude = ds.createDimension('longitude', len(lon))
   
    time = ds.createVariable('time', np.float32, ('time',))
    latitude = ds.createVariable('latitude', np.float32, ('latitude',))
    longitude = ds.createVariable('longitude', np.float32, ('longitude',))

    # check if the data is 2d or 3d
    if len(data.shape) == 4: # 4D array
        pet_val = ds.createVariable(varname, 'f4', ('time','hours','latitude','longitude'), zlib=True)
        time.units = tunits  
        time.calendar = 'proleptic_gregorian'
        time[:] = timevals
        latitude[:] = lat
        longitude [:] = lon
        pet_val[:,:,:,:] = data
        pet_val.units='mm/hr'
        latitude.units='degrees_north'
        longitude.units='degrees_east'

    elif len(data.shape) == 3: # 3D array
        pet_val = ds.createVariable(varname, 'f4', ('time','latitude','longitude'), zlib=True)
        time.units = tunits  
        time.calendar = 'proleptic_gregorian'
        time[:] = timevals
        latitude[:] = lat
        longitude [:] = lon
        pet_val[:,:,:] = data
        pet_val.units='mm/hr'
        latitude.units='degrees_north'
        longitude.units='degrees_east'
    
    elif len(data.shape) == 2: # 2D array
        pet_val = ds.createVariable(varname, 'f4', ('latitude','longitude'), zlib=True)
        latitude[:] = lat
        longitude [:] = lon
        pet_val[:,:] = data
        pet_val.units='mm/hr'
        latitude.units='degrees_north'
        longitude.units='degrees_east'

    else:
        raise ValueError('the function can only write a 2D, 3D and 4D array data!')

    ds.close()
    
    return None   
# ======================================================================= #
if __name__ == '__main__':
    start = dt.datetime.now()
    print('Seasonal PET forecast in progress ...')
    forecast_wrapper(tercile_forecast_file, outputpath, startyear, startdate, enddate, locname, number_ensm, tempAdj, seasonName, mask_file)
    print('Seasonal PET forecast files finished successfully.')
    
    end=dt.datetime.now()
    print('Time of run: %s'%(end - start))

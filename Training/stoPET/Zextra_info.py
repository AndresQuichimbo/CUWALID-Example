
# Regional stoPET run (Kenya)
#latval_min = -1.6
#latval_max = 1.1
#lonval_min = 35.9
#lonval_max = 40.1 

# Regional stoPET run (Ethiopia)
#latval_min = 7.5
#latval_max = 10.0
#lonval_min = 38.5
#lonval_max = 41.5 

# Regional stoPET run (Somalia)
#latval_min = 8.3
#latval_max = 10.5
#lonval_min = 42.0
#lonval_max = 46.0


# Regional stoPET run (HAD)
#latval_min = -7.0
#latval_max = 16.0
#lonval_min = 31.0
#lonval_max = 52.1 


# this is where you provide a sting of name to identify your region or point e.g. 'tana_basin'
#locname = 'TanaBasin' # Kenya
#locname = 'UAVBasin'  # Ethiopia
#locname = 'ODBasin'   # Somalia
#locname = 'HAD'       # HAD


# This is the file containing the ICPAC seasonal tercile temperature forecast.
# provide the full path where it is located

#tercile_forecast_file = 'C:/Users/fp20123/Dropbox/CUWALID/new_stopet/shapefiles/TanaBasinTfMAM2024.nc'     # Kenya
#tercile_forecast_file = 'C:/Users/fp20123/Dropbox/CUWALID/new_stopet/shapefiles/UAVBasin_TempMAM2024.nc'   # Ethiopia
#tercile_forecast_file = 'C:/Users/fp20123/Dropbox/CUWALID/new_stopet/shapefiles/ODBasin_TempMAM2024.nc'     # Somalia
#tercile_forecast_file = '/user/home/fp20123/new_stopet/ICPAC_TempF_MAM2022_HAD.nc'  

## mask file
#mask_file = '/user/home/fp20123/new_stopet/mask_for_HAD.nc'

#############################################################
# numba parallel run function  
# decorate the function  
@jit(nopython=True, parallel=True)  
def forecast_with_tercile(ori_data, tercileTf, time, tunits, lats, lons, 
                          outputpath, locname, number_ensm,
                          tempAdj, startdate, enddate, startyear):
 
  # file name of the adjusted PET from stopet
  fname = 'AdjstoPET_%s_%s_%s_%s.nc'%(tempAdj, startdate, enddate, startyear)
  # create array to append data
  ens_f = np.ones((number_ensm, ori_data.shape[0], ori_data.shape[1], ori_data.shape[2])) * -1
   
  # loop through files and extract array of PET accordinglly
  for i in prange(ori_data.shape[1]): # row # use parallel range
    for j in range(ori_data.shape[2]): # col
      # Here we need to put exceptions for the grids with empty seasonal forecast 
      # like the ocean area where there is no forecast. 
      # We do that by jumping the grid to save computationonal time.
      # all values will be -1 for those grids so easy to mask as thre are no negative PET in stoPET.
      if np.sum(tercileTf[:,i,j]) != 100.:
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
          # print('For %s choice array is %s, inx=%s'%(v,choice_range,inx))
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
              filepath = outputpath + locname + '_A_E%s_StoPET/'%ens
              # read the file
              nc = Dataset(filepath + fname)
              pet = nc.variables['pet'][:,i,j]
              ens_f[ens_v,:,i,j] = pet 
              #print(v,filepath)
            elif v == 1:
              filepath = outputpath + locname + '_N_E%s_StoPET/'%ens
              # read the file
              nc = Dataset(filepath + fname)
              pet = nc.variables['pet'][:,i,j]
              ens_f[ens_v,:,i,j] = pet
              #print(v,filepath)
            else:
              filepath = outputpath + locname + '_B_E%s_StoPET/'%ens
              # read the file
              nc = Dataset(filepath + fname)
              pet = nc.variables['pet'][:,i,j]
              ens_f[ens_v,:,i,j] = pet
              #print(v,filepath)
          # find the remain numbers that are not choosen to go for the next one.
          # doing this avoids over writing of array.
          choice_range=np.asarray(list(set(choice_range).difference(ensnum)))
          start = end # this updatesthe starting point to create array 

  # write the final ensembles on a netcdf file
  # create a folder to save the data
  if not os.path.isdir(outputpath + 'ensemble_forecast/'):
    os.mkdir(outputpath + 'ensemble_forecast/')
  
  for f in range(ens_f.shape[0]):
    data = ens_f[f,:,:]
    outpath = outputpath + 'ensemble_forecast/'
    filename = (outpath + 'Forecast_PET_%s_ens_%s_' + fname)%(locname,f)
    varname = 'pet'
    timevals = time[:]
    forecast_nc_write(data, lats, lons, varname, timevals, tunits, filename)
  
  return None          


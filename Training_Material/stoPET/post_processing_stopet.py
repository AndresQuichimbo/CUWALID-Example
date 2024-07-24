from netCDF4 import Dataset, num2date
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as sps
import scipy.optimize
import pandas as pd
import datetime as dt
from collections import Counter
from mpl_toolkits.basemap import Basemap, maskoceans
import matplotlib.colors as mcolors
import os

from matplotlib import rcParams
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['xtick.labelsize'] = 10 
# ===============================================================#
def stopet4dryp(filepath, fname, seasonswitch, startdate, enddate):
    """
    This function reshape and rename the stoPET output to fit into the DRYP
    model input requirement of PET.
    The first requirment is the data need to be a 3D vale with (time, lat,lon).
    The secoond requiremnt is the file name sould have a prefix_year.nc format.
    
    param fname: the file name for the output of the stoPET model PET
    param seasonswithch: this is a switch  0 for all year and 1 to choose a season period  
    param startdate: the starting day of year for the seaosn needed
    param enddate: the end day of year for the season needed
    output data: The file containing the required dimention and file name for DRYP model 
    """
    # reasd the variables
    nc = Dataset(filepath + fname)  
    lats = nc.variables['latitude'][:]
    lons = nc.variables['longitude'][:]
    pet = nc.variables['pet'][:,:,:,:] 
    
    # extract season values
    if seasonswitch == 1:
      ## start date is reduced by one as python start count from 0
      pet = pet[startdate-1:enddate,:,:,:]  
    else:
      pass
    
    # change the dimention to (time, lat,lon)
    # flatten the first two dimensions (day, hour)
    new_pet = pet.reshape(-1, *pet.shape[-2:])
    
    # write the new PET value to netcdf file
    # split the file name
    f = fname.split('.')
    x = f[0].split("_")
    year = x[0]
    method = x[1]
    suffix = x[2]
    if seasonswitch == 1:
      filename = filepath + '%s_%s_%s_%s_%s.nc'%(suffix, method, startdate, enddate, year)
    else:
      filename = filepath + '%s_%s_%s.nc'%(suffix, method, year)
    tunits = 'hours since %s-01-01 00:00'%year
    nc_write(new_pet, lats, lons, 'pet', tunits, filename, startdate)
    
    return None
    
def nearest_point(lat_var, lon_var, lats, lons):
    """
    This function identify the nearest grid location index for a specific lat-lon
    point.
    :param lat_var: the latitude
    :param lon_var: the longitude
    :param lats: all available latitude locations in the data
    :param lons: all available longitude locations in the data
    :return: the lat_index and lon_index
    """
    # this part is to handle if lons are givn 0-360 or -180-180
    if any(lons > 180.0) and (lon_var < 0.0):
        lon_var = lon_var + 360.0
    else:
        lon_var = lon_var
        
    lat = lats
    lon = lons

    if lat.ndim == 2:
        lat = lat[:, 0]
    else:
        pass
    if lon.ndim == 2:
        lon = lon[0, :]
    else:
        pass

    index_a = np.where(lat >= lat_var)[0][-1]
    index_b = np.where(lat <= lat_var)[0][-1]

    if abs(lat[index_a] - lat_var) >= abs(lat[index_b] - lat_var):
        index_lat = index_b
    else:
        index_lat = index_a

    index_a = np.where(lon >= lon_var)[0][0]
    index_b = np.where(lon <= lon_var)[0][0]
    if abs(lon[index_a] - lon_var) >= abs(lon[index_b] - lon_var):
        index_lon = index_b
    else:
        index_lon = index_a

    return index_lat, index_lon   

def seasonal_nc_write(data, lat, lon, varname, tunits, filename, startdate):
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
    hours = ds.createDimension('hours', 24)
   
    time = ds.createVariable('time', np.float32, ('time',))
    hours = ds.createVariable('hours', np.float32, ('hours',))
    latitude = ds.createVariable('latitude', np.float32, ('latitude',))
    longitude = ds.createVariable('longitude', np.float32, ('longitude',))

    # check if the data is 2d or 3d
    if len(data.shape) == 4: # 4D array
        pet_val = ds.createVariable(varname, 'f4', ('time','hours','latitude','longitude'), zlib=True)
        time.units = tunits  
        time.calendar = 'proleptic_gregorian'
        time[:] = np.arange(((startdate-1)*24),(((startdate-1)*24) + data.shape[0]))
        hours[:] = np.arange(data.shape[1])
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
        time[:] = np.arange(((startdate-1)*24), (((startdate-1)*24) + data.shape[0]))
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




def leap_remove(timeseries):
    """
    This function removes leap days from a time series 
    param timeseries: array containing daily time series
    param datastartyear: start year of the input data
    output data: time series with the leap days removed. 
    """
    
    # system only takes 365 days in each year so we
    # remove leap year values from the long term time series
    t = np.arange(59*24, (59*24) + 24).astype(int)
    data = np.delete(timeseries, t, axis=0)

    return data
    
    
def running_mean(timeseries, n):
    """
    This function calculate the running mean of a timeseries data.
    param timeseries: array containing the time series
    param n: the number for the running mean
    output val: time series with the running mean value 
    """
    val =[]
    for i in range(0,len(timeseries) - n):
        x= np.mean(timeseries[i: i+ n])
        val = np.append(val,x)
    return val
    

def aggregate_data(timeseries, period):
    """
    This function aggregate the hourly timeseries data to the desired period.
    param timeseries: array containing the time series
    param period: the period required for aggregation (daily, monthly, annual)
    output output: time series with the aggregated value for the specified period.
    """
    # make a reshape of the time series to have 365 by 24 array
    data_re = np.reshape(timeseries,(int(len(timeseries)//24),24))
    
    # make a daily PET
    if period == 'day':
        output = np.sum(data_re, axis=1)
    # make a monthly PET
    elif period == 'month':
        pet_day = np.sum(data_re, axis=1)
        output = []
        m =[0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
        for i in range(1,len(m)):
            month_pet = np.sum(pet_day[int(m[i-1]) : int(m[i])])  # monthly PET
            output = np.append(output, month_pet)
    # make annual PET
    elif period == 'year':
        output = np.sum(timeseries)
    else:
        raise ValueError("There is a problem on the period value. Please provide 'day','month', or 'year'")
    
    return output
 

def timeseries_plot(data, xlabel, ylabel, title, plotpath, fname):
    """
    This function plot any timeseries value.
    param data: array containing the time series data
    param xlabel: the x axis lable in string (e.g. 'DOY')
    param ylabel: the y axis label in string (e.g. 'PET ($\mathbf{mm\,h^{-1}}$)')
    param title: the title of the plot in string (e.g. 'Daily peak PET for Kenya')
    param plotpath: the folder where the plot will be saved in string (e.g. './plots/')
    param fname: the file name for the plot with extension in string (e.g. 'ts_plot.png')
    output none: plot saved in the location specified.
    """
    # ts plot
    fig=plt.figure()
    plt.plot(data,'k')
    plt.ylabel(ylabel)  
    plt.xlabel(xlabel)  
    plt.title(title,fontweight='bold') 
#    plt.tight_layout() 
#    plt.savefig(plotpath + fname,bbox_inches='tight',dpi=600)
#    plt.close() 
    

def comparison_timeseries_plot(data_1, data_2, label_1, label_2, xlabel, ylabel, title, plotpath, fname):
    """
    This function plot any timeseries value.
    param data_1: array containing the time series data for first data
    param data_2: array containing the time series data for second data
     param label_1: the lable for the first data in string (e.g. 'hPET')
    param label_2: the label for the second data in string (e.g. 'Adj hPET')
    param xlabel: the x axis lable in string (e.g. 'DOY')
    param ylabel: the y axis label in string (e.g. 'PET ($\mathbf{mm\,h^{-1}}$)')
    param title: the title of the plot in string (e.g. 'Daily peak PET for Kenya')
    param plotpath: the folder where the plot will be saved in string (e.g. './plots/')
    param fname: the file name for the plot with extension in string (e.g. 'ts_plot.png')
    output none: plot saved in the location specified.
    """
    # ts plot for two datasets for comparison
    fig=plt.figure()
    plt.plot(data_1,'k', label=label_1)
    plt.plot(data_2,'k--', label=label_2)
    plt.ylabel(ylabel)  
    plt.xlabel(xlabel)  
    plt.title(title,fontweight='bold') 
    plt.legend(loc='best')
#    plt.tight_layout() 
#    plt.savefig(plotpath+fname,bbox_inches='tight',dpi=600)
#    plt.close() 

  
def comparison_density_plot(data_1, data_2, label_1, label_2, xlabel, ylabel, title, plotpath, fname):
    """
    This function plot any timeseries value desity plot.
    param data_1: array containing the time series data for first data
    param data_2: array containing the time series data for second data
     param label_1: the lable for the first data in string (e.g. 'hPET')
    param label_2: the label for the second data in string (e.g. 'Adj hPET')
    param xlabel: the x axis lable in string (e.g. 'PET ($\mathbf{mm\,h^{-1}}$)')
    param ylabel: the y axis label in string (e.g. 'Density')
    param title: the title of the plot in string (e.g. 'Daily peak PET for Kenya')
    param plotpath: the folder where the plot will be saved in string (e.g. './plots/')
    param fname: the file name for the plot with extension in string (e.g. 'ts_plot.png')
    output none: plot saved in the location specified.
    """
    # Density plot
    fig=plt.figure()
    # Draw the density plot
    sns.kdeplot(data_1,  color = 'k',label = label_1)
    # Draw the density plot
    sns.kdeplot(data_2, color = 'orange',label = label_2)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title,fontweight='bold') 
    plt.legend(loc='best')
#    plt.tight_layout() 
#    plt.savefig(plotpath+fname,bbox_inches='tight',dpi=600)
#    plt.close() 
# =========================================================================##

# SPATIAL PLOT FUNCTIONS
   
def plot_spatial(data, lats, lons, cmap , title, cbar_label, climin, climax, plotpath, figfname):
    fig = plt.figure()
    m = Basemap(projection='cyl', llcrnrlat=min(lats), urcrnrlat=max(lats), llcrnrlon=min(lons),
                urcrnrlon=max(lons), resolution='l')

    cs4 = plt.imshow(data, interpolation='nearest', cmap=cmap,
                     extent=[min(lons), max(lons), min(lats), max(lats)]) 
    m.drawcoastlines(linewidth=1.0)
    m.drawcountries(linewidth=0.75)
    parallels=np.arange(-90.,90.,10.0)
    meridians=np.arange(0.,360.,10.0)
    m.readshapefile("./Tana_basin_wgs84",'Watersheds')
    m.drawlsmask(land_color=(0,0,0,0), ocean_color='white', lakes=False) 
    plt.title(title, fontweight='bold', loc='center')
    cb4 = plt.colorbar(cs4, label=cbar_label, shrink=0.4, pad=0.02, extend='both', orientation='horizontal')
    cb4.mappable.set_clim(climin, climax)
#   plt.tight_layout()  
#    fig.savefig(plotpath + figfname, bbox_inches='tight', dpi=600)
#    plt.close()


# *********************************************** #
def check_ts():
    filepath = '/user/home/fp20123/stoPET/result/TanaBasin_E0_StoPET/'
    fname = '2022_2_stoPET.nc'
    nc1 = Dataset(filepath + fname)
    dd = nc1.variables['pet'][:,:,:,:]
    lats = nc1.variables['latitude'][:]
    lons = nc1.variables['longitude'][:]
    dval = dd[5,14,:,:]
    plot_spatial(dval, lats, lons, 'bwr_r' , '', 'mm/hr', '0.', '1.0','./', 'check.png')
    
    data1 = dd[:,:,5,10]
    
    # data 2
    nc2 = Dataset(filepath + 'stoPET_2_274_365_2022.nc')
    data2 = nc2.variables['pet'][:,5,10]
    
    # compare data
##    for i in range(273, 365):
##      data = data1[i,:] - data2[i*24 :(i*24)+24]
##      print(data)
    
    data = data1[-1,:] - data2[-24: ]
    plt.plot(data1[-1,:])
    plt.plot(data2[-24: ]) 
    plt.show()
    
    print(np.sum(data2))

def check_ens():
    ens=[]
    for i in range(0,30):
      filepath = '/user/home/fp20123/stoPET/result/TanaBasin_stoPET/' #TanaBasin_E%s_StoPET/'%i
      fname = 'E%s_AdjstoPET_2_274_365_2022.nc'%i
      nc1 = Dataset(filepath + fname)
      data1 = nc1.variables['pet'][-24:,5,10]
      ens.append(data1)
    ens=np.array(ens)
    print(ens.shape) 
    for i in range(0,30): 
      plt.plot(ens[i,:])
    plt.show()
    
def loop_TanaBasin():
    for i in range(0,30):
      filepath = '/user/home/fp20123/stoPET/result/TanaBasin_E%s_StoPET/'%i
      fname = '2022_2_stoPET.nc'
      seasonswitch = 1
      startdate = 274 
      enddate = 365
      stopet4dryp(filepath, fname, seasonswitch, startdate, enddate)

def loop_TanaBasin_rename():
    for i in range(0,30):
      filepath = '/user/home/fp20123/stoPET/result/TanaBasin_E%s_StoPET/'%i
      fnameall = filepath + 'AdjstoPET_2_274_365_2022.nc'
      fname='AdjstoPET_2_274_365_2022.nc'
      newfname = '/user/home/fp20123/stoPET/result/TanaBasin_stoPET/E%s_%s'%(i,fname)
      command = 'mv %s %s'%(fnameall,newfname)
      os.system(command)
      print(fname)

def check_dates():
    fname='AdjstoPET_2_274_365_2022.nc'
    newfname = '/user/home/fp20123/stoPET/result/TanaBasin_stoPET/E%s_%s'%(0,fname)
    nc = Dataset(newfname)
    time=nc.variables['time']
    dates = num2date(time[:],time.units,time.calendar )
    print(dates)
          
# *********************************************** #    
if __name__ =='__main__':
##    loop_TanaBasin()
##    check_ts()
##    check_ens()
##    loop_TanaBasin_rename()
    check_dates()

  
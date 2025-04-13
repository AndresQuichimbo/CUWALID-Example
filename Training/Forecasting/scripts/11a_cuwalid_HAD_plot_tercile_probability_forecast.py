#import pyproj as pp
import numpy as np
import xarray as xr
import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import CUWALID_forecast_tools as cuwalid
import CUWALID_view_tool as cuwalidplt
from config_plot_cuwalid import *

"""This function creates a figure from the tercile forecats
file. Variabkes names of the file must be: "AN", "NN, "BN".

Comment lines if variables can accesed from the config_plot_cuwalid
"""


# Specify model name, This will be the root name for the forecasting
model_name = "HAD_IMERGba_sim0"
model_name = "MAM_2022_realization"

# Path of model output files
#model_path = "D:\HAD\training\forecast\regional\outputs/"
model_path = "/home/c1755103/HAD/HAD_output/"

# path for post processing files, i.g. forecasting
# Specific folders will be created inside this paht to store different
# types of lie formats
# /fig: for any king of figure
# /netcdf: for *.nc files
# /raster: for *.asc files
# /csv: for comma delimited files, i.g. *.csv
#postpp_path = "D:\HAD\training\forecast\regional\postpp/"
postpp_path = "/home/c1755103/HAD/HAD_postpp/"
postpp_path = "D:/HAD/postpp/"

# specify season
#season = [None, "OND", "MAM"]

# load dataset of mask for basin and streams
path_mask = "../HAD/WS/input_model/HAD_mask_utm.asc"
path_river =  "../HAD/WS/input_model/HAD_riv_length_utm.asc"


# path of shapefile to include in the plot
#shapefile_county = "D:/HAD/data/gis/Horn_Africa/Horn_africa_contry.shp"
shapefile_county = "/home/cuwalid/Datasets/data/shp/wgs84/HAD_regional_basin.shp"

# specified fields
field = cuwalid.drop_false_keys(variables)

#ifname = fname_ensamble.replace("_VVV", "")

iyear = 2022
iseason = "MAM"

#fname = "D:/HAD/postpp/netcdf/HAD_IMERGb_D2E_sim_" + iseason + "_probabilistic_tercile_forecast_region.nc"
#fname = "D:/HAD/postpp/netcdf/MAM_2022_realization_pre_MAM_2022_probabilistic_tercile_forecast.nc"
#fname = "D:/HAD/postpp/netcdf/MAM_2022_realization_pet_MAM_2022_probabilistic_tercile_forecast.nc"

for ivar in field:
	# save as NETCDF files
	if iseason is None:
		fname = postpp_path+"netcdf/" + model_name + "_" +ivar+"_"+str(iyear)+"_probabilistic_tercile_forecast.nc"
	else:
		fname = postpp_path+"netcdf/" + model_name + "_" +ivar+"_"+iseason+"_"+str(iyear)+"_probabilistic_tercile_forecast.nc"
		
	data = xr.open_dataset(fname)
	im = cuwalidplt.plot_probabilistic_tercile_forecast(data,
			title="Probabilistic Forecasting\n"+
				cuwalidplt.get_label_variable(ivar),
			reproject=True, fshapefile=shapefile_county,
			fmask=path_mask)
		
	if iseason is None:
		fname_fig = postpp_path+"fig/" + model_name + "_" +ivar+"_"+str(iyear)+"_probabilistic_tercile_forecast.png"
	else:
		fname_fig = postpp_path+"fig/" + model_name + "_" +ivar+"_"+iseason+"_"+str(iyear)+"_probabilistic_tercile_forecast.png"
		
	#fname_fig = "D:/HAD/postpp/fig/IMERGag_sim0_MAM_tercile_forecasting_example.png"
	plt.savefig(fname_fig, dpi=300)
#plt.show()
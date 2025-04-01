# Specify model name, This will be the root name for the forecasting
#model_name = "HAD_IMERGba_sim0"
#model_name = "MAM_2022_realization"
model_name = "MAM_2022_realization_test"


# Path of model output files
#model_path = "D:\HAD\training\forecast\regional\outputs/"
#model_path = "/home/c1755103/HAD/HAD_output/"
#model_path = "/home/cuwalid/training/forecast/regional/outputs/"#_13_grid.nc
model_path = "/shared/training/forecast/regional/outputs/"#_13_grid.nc

# path for post processing files, i.g. forecasting
# Specific folders will be created inside this paht to store different
# types of lie formats
# /fig: for any king of figure
# /netcdf: for *.nc files
# /raster: for *.asc files
# /csv: for comma delimited files, i.g. *.csv
#postpp_path = "D:\HAD\training\forecast\regional\postpp/"
#postpp_path = "/home/c1755103/HAD/HAD_postpp/"
#postpp_path = "/home/cuwalid/training/forecast/regional/postpp/"
#postpp_path = "/home/<username>/training/forecast/regional/postpp/"
postpp_path = "/home/aquichimbo/training/forecast/regional/postpp/"

# path of threshold datasets, it can be the threshold values
# it can be the sam as the post processing folder
#threshold_path = "/home/c1755103/HAD/HAD_postpp/"
#threshold_path = "/home/cuwalid/training/historical/regional/postpp/netcdf/HAD_IMERGba_sim0_MAM_extremes_quantiles.nc"
#threshold_path = "/home/<username>/training/historical/regional/postpp/netcdf/HAD_IMERGba_sim0_MAM_extremes_quantiles.nc"

threshold_path = "/home/aquichimbo/training/historical/regional/postpp/netcdf/HAD_IMERGba_sim0_MAM_extremes_quantiles.nc"

# specify season
#season = [None, "OND", "MAM"]
season = ["MAM"]

# Parameters for model 

# specify historical period
start_year = 2003
end_year = 2023

# Specified variables to process
variables = {
'pre' : True,
'pet' : True,
'aet' : True,
'tht' : True,
'egw' : True,
'inf' : False,
'run' : False,
'rch' : True,
'fch' : True,
'gdh' : False,
'dis' : True,
'tls' : False,
'wte' : True,
"twsc" : True
}


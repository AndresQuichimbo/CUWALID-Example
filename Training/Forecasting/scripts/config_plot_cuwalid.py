# Specify model name, This will be the root name for the forecasting
model_name = "HAD_IMERGba_sim0"

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

# specify season
season = [None, "OND", "MAM"]

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
"twsc" : True,
"wrsi" : True,
}
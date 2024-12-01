import sys
sys.path.append("C:/Users/Edisson/Documents/GitHub/CUWALID")
#sys.path.append("/home/cuwalid/CUWALID/")
import os
import numpy as np
import pandas as pd
import cuwalid.forecasting.main_impact_forecast as fcast

fconfig = "/home/cuwalid/training/forecasting_model_files/impact_forecast_input_ICPAC.json"
fconfig = "C:/Users/Edisson/Documents/GitHub/CUWALID-Example/input/impact_forecast_input.json"

fcast.plot_maps_json(fconfig)
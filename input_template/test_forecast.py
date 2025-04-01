import sys
import time
sys.path.append("/home/cuwalid/CUWALID")
from cuwalid.forecasting.main_hydro_forecast import run_hydro_forecast

fname = "/home/cuwalid/training/forecasting_model_files/forecast_input.json"
start_time = time.time()
run_hydro_forecast(fname)
end_time = time.time()

print(f'Forecast ran in: {end_time-start_time}')
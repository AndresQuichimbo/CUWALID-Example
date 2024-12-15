import sys
import time
sys.path.append("/home/cuwalid/CUWALID")
from cuwalid.main_cuwalid_ICPAC import run_cuwalid

fname = "/home/cuwalid/training/forecasting_model_files/cuwalid_input_ICPAC.json"
start_time = time.time()
run_cuwalid(fname)
end_time = time.time()

print(f'CUWALID ran in: {end_time-start_time}')
import time
from cuwalid.main_cuwalid import run_cuwalid



start_time = time.time()
run_cuwalid("input/cuwalid_input_ICPAC.json")
end_time = time.time()

print(f'CUWALID ran in: {end_time-start_time}')
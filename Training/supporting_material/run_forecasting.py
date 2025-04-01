import time
from cuwalid.forecasting.main_impact_forecast import run_forecast

start_time = time.time()
run_forecast("input/forecast_input.json")
end_time = time.time()

print(f'Forecast ran in: {end_time-start_time}')
import os

filename = 'forecast/regional/OND_2022/dataset/pet/Forecast_PET_HAD_ens_2022_OND_0.nc'


print(f"Current user: {os.getlogin()}")
print(f"File: {filename}")
print(f"File exists: {os.path.exists(filename)}")
print(f"Writable: {os.access(filename, os.W_OK)}")
print(f"Directory: {os.path.dirname(filename)}")
print(f"Directory writable: {os.access(os.path.dirname(filename), os.W_OK)}")
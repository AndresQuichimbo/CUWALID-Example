# CUWALID-Example
An example of how to install and run the CUWALID PyPi package

These steps assume you are starting from the very beggining and need to install python. If you already have a compatable python version installed (3.9-3.11 are tested) then you can skip ahead.

## Step 1:

Install python (recommended to use python 3.11) from the link here: 
https://www.python.org/downloads/release/python-3119/

Whilst going through the installation steps, please ensure you tick the box saying "Add Python to system path"

## Step 2:
Open the directory you want to work in and ensure that python is working there by typing the following in you terminal
```
python --version
```
It should print out your python version if everything is working correctly

Now create a virtual environment (This step is recommended but not technically necessary) by running the following command:
```
python -m venv test_env
source test_env/bin/activate  # On Windows use `test_env\Scripts\activate`
```
Now your environment is created and is activated

## Step 3:
Now you can install the package,

Run the command:
```
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple CUWALID
```

Hopefully this will run without any errors and all other necessary packages will be installed.

## Step 4:
In this GitHub repository is an example of the code you will need to run a simple model with DRYP, it includes a run files and some practice data for the dryp model. You can open the 'run_*' files to see how you can implement the models into your own code.

For running the DRYP model it should be as simple as running the command (Ensure your environment is activated):
```
python run_dryp.py
```

The output should be placed in a new folder called 'dryp_output'.

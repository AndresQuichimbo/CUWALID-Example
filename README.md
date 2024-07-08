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
python -m venv venv_name
source test_env/bin/activate  # On Windows use `test_env\Scripts\activate`
```
Now your environment is created and is activated

## Step 3:
Now you will need to install the package, during this step it will ask for an API token which i have left at the bottom of this step to copy and paste into the terminal.

Run the command:
```
pip install -i https://test.pypi.org/simple/ CUWALID
```

API TOKEN (DON'T SHARE) *It includes the begginging part -> 'pypi-':
```
pypi-AgENdGVzdC5weXBpLm9yZwIkYjc3NjM5YWUtNzZlZi00YzZkLWI1YTAtYzc5YTI4ZmYwY2E5AAIPWzEsWyJjdXdhbGlkIl1dAAIsWzIsWyJjNzRlYTk4My0yNmI4LTRlM2ItYWFlMy0wZGI0NjczMjM4YzQiXV0AAAYgHQJagS3PIv8C5N3H0IhAb3x5jOaLZvDLqK2fbwHdzJ4
```

Hopefully this will run without any errors and all other necessary packages will be installed.

## Step 4:
In this GitHub repository is an example of the code you will need to run a simple model with DRYP, it includes a 'run.py' file that can be used to run the DRYP model, and a 'input' folder which contains the input for the model.

So it should be as simple as running the command (Ensure your environment is activated):
```
python run.py
```

The output should be placed in a new folder callout 'test_output'.

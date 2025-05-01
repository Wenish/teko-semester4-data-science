# TEKO Semester 4 Data Science


## Developer setup

#### 1. Install the latest Python v3.x on your machine.

https://www.python.org/

#### 2. Initialize your venv

`python -m venv .venv`

#### 3. Activate your environment

For Linux Based OS or Mac-OS

`source .venv/bin/activate`

For Windows with CMD

`.\.venv\Scripts\activate.bat`

#### 4. Install the project dependencies

Run those commands in the root folder of the repository:

`pip install --upgrade pip`

`pip install -r requirements.txt`


#### 5. register .venv as Jupyter-Kernel

`python -m ipykernel install --user --name=jupiter-venv --display-name "Python (jupiter-venv)"`

#### 6. Change Juptier Kernel

Change Kernel on Jupiter Notebook to the registered venv.

In VS Code you can open die .ipynb file and the kernel to select is on the top right.

## Freeze Dependencies

Run this command in the root folder of the repository:

`pip freeze > requirements.txt`

## Debug

Import pdb in the file you want to start the debug:

`import pdb`

Add this line where the debug should start:

`pdb.set_trace()`
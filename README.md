# shop
our-shop

## Setup
### Backend
Setup a virtual environment in ./backend.
```
py -m venv .vevn
```

Activate said virtual environment by running the appropriate version of the activate script. Your prompt should change to indicate that indeed the venv is active. You can also check by seeing if sys.prefix points to the venv python. Note that on Windows this does not work in the vscode terminal.

```
source ./.venv/bin/activate
```

To install the backend dependencies go to /backend and run:  
`pip install -r requirement.txt`  

For development purposes you will want to install the dev dependencies as well:
`pip install -r ./dev_requirement.txt`  

Please note that this will install the dependencies globally if you haven't setup a venv.

When you want to add a new dependency, run:  
`pip freeze`  
and copy the specific dependency you need to any of the requirements files.  

### Frontend
To install dependencies, go to /frontend and run:  
`npm install`  

## Code style conventions
#### Imports / Exports
Imports should be ordered: npm / pip installed packages come first seperated by an empty line with any local files

#### Frontend Folder structure 
The application uses a variation of 'Atomic design' by Brad Frost. The difference between the original and this is that here we don't have templates, but have added a root category.

## Development
### Backend
You can use the following command to watch the py files and restart the server on any changes:
`watchmedo auto-restart --directory=./src --pattern='*.py;*.txt' --recursive --kill-after 1 python3 ./src/main.py`

## Tasks:
Find a way to automate py cli scripts ( py index.py mode=development => pyscripts run start-dev )

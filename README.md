# shop
our-shop

## Setup
### Backend
Setup a virtual environment in ./backend.
```
cd ./backend/
py -m venv .vevn
```

Activate said virtual environment by running the appropriate version of the activate script. Your prompt should change to indicate that indeed the venv is active. You can also check by seeing if sys.prefix points to the venv python. Note that on Windows this does not work in the vscode terminal.

```
cd ./backend/
.venv/Scripts/activate.bat
```

To install all backend dependencies go to /backend and run:  
`pip install -r requirement.txt`  
Please note that this will install the dependencies globally.  

When you want to add a new dependency, run:  
`pip freeze`  
and copy the specific dependency you need to the requirements.txt file.  


### Frontend
To install dependencies, go to /frontend and run:  
`npm install`  

## Keeping track of dependencies
### Backend
I recommend manually adding newly installed dependencies by running 
`pip freeze`  
and copying the dependency name and version over to requirements.txt as the forementioned command also returns dependencies that are required by the venv itself.

## Code style conventions
### Backend


### Frontend
#### Folder structure
The application uses a variation of 'Atomic design' by Brad Frost. The difference between the original and this is that here we don't have templates, but have added a root category.
# To create a new project from a cloned repository:
- Opened PycharmProjects and made sure it does not have .git and venv file
- inside this directory in the terminal made git clone the tdd repo
- from the file chose new project chose the location to be the repo tdd-class---> create project from existing 
this created a clean virtual environment which is activated in the terminal

# some changes to the requirements
- Deleted Ww from line 2 in the requirements
- added pydantic to the requirement
- installed requirement plugin
- the requirement file will check if some requirements are not satisfied and ask to install them
- installed tox and from the tox.ini file deleted --basement="{environment}" {postgres} from line 15
- jwd
- bcrypt
- PyJWD

# to go to the fastapi version 
run: 
```commandline
git getch --tags
git checkout tags/v0.1-fastapi -b fastapi-latest-version
```

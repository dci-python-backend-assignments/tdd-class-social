


To create a new project from a cloned repository:
- Opened PycharmProjects and made sure it does not have .git and venv file
- inside this directory in the terminal made git clone the tdd repo
- from the file choosed new project choosed the location to be the repo tdd-class---> create project from existing 
this created a clean virtual enviroment which is activated in the terminal
- Deleted Ww from line 2 in the requirements
- added pydantic to the requirement
- installed requirement pluging
- the requirement file will check if some requirement are not satisfied and ask to install them
- installed tox and from the tox.ini file deleted --basetemp="{envtmpdir}" {posargs} from line 15
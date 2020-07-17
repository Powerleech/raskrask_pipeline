This project requires a 'local_settings.py' to be created manually for this project.
Example local_settings.py is in the bottom of this readme. 
It can be copy pasted without issue in its current form, though you will need to configure SQLALCHEMY_DATABASE_URI.
Lines in the local_settings.py example starting with '#' are commented out lines, to serve as an example.

to run the project, you must run interface.py
e.g. python3 interface.py

*** INSTALL AND CONFIGURE THE PROJECT ***

Python3 must be installed.
virtualenv must be installed on linux, otherwise anaconda has a built in venv.


to use virtualenv on linux:
Navigate into the project folder you intend to use and follow these commands

python3 -m venv python3-virtualenv     #creates a venv called python3-virtualenv
source python3-virtualenv/bin/activate #activates that env
deactivate                             #deactivates the venv

pip freeze                             #shows you what packages are installed in the venv
pip install -r requirements.txt        #how to install needed packages for the project in the venv from the requirements.txt


*** LOCAL_SETTINGS *** + example

'SQLALCHEMY_DATABASE_URI' should be a connection string to a database with the appropriate adapter
Keep in mind a pip install for the appropriate adapter may be required as the current 'requirements.txt' only includes PyMySQL==0.9.3 for mariadb
FILE_PATH when set False will write otu the files to a default directory, as a subdirectory of the project called /data/
if you specify a file path, you must use forward slashes '/' in the file path
METADATA_ON when enabled will print out all the database objects and their fields, with then umber of rows in that object
DATABASE_IGNORE_LIST when left empty will extract all tables from the db, any table names written in there wont be extracted.
TESTRUN_OR_LIVERUN is applied to the database objects, such that a test run will only take 2 rows form the database objects, live will take all
CSV_OR_JSON determines what file type is written out

# -*- coding: utf-8 -*-
SQLALCHEMY_DATABASE_URI = ""
#SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/test2"
FILE_PATH = False
#FILE_PATH = r"C:/Users/lenovo/Documents/GitHub/raskrask_pipeline/data/"
METADATA_ON = False #False or True
DATABASE_IGNORE_LIST = []
#DATABASE_IGNORE_LIST = ["yotporeviews", "yogainstructors"]
TESTRUN_OR_LIVERUN = "test" #only use the values 'test' or 'live'
CSV_OR_JSON = "csv" #only use the values 'csv' or 'json'
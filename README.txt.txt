This project requires a 'local_settings.py' to be created manually for this project.
Example local_settings.py is in the bottom of this readme.



























'SQLALCHEMY_DATABASE_URI' should be a connection string to a database with the appropriate adapter
Keep in mind a pip install for the appropriate adapter may be required as the current 'requirements.txt' only includes PyMySQL==0.9.3

# -*- coding: utf-8 -*-

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/test2"
#FILE_PATH = False
FILE_PATH = r"C:\Users\lenovo\Documents\GitHub\raskrask_pipeline\json_data\\"


DATABASE_IGNORE_LIST = []
#DATABASE_IGNORE_LIST = ["yotporeviews", "yogainstructors"]

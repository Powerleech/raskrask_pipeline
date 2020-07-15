This project requires a 'local_settings.py' to be created manually for this project, as seen in the 'interface.py' imports.
Only a single variable exists 'local_settings.py' which is 'SQLALCHEMY_DATABASE_URI'.
The value of 'SQLALCHEMY_DATABASE_URI' should be a connection string to a database with the appropriate adapter
- e.g: SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/test2'
This would be a connection to a local mariadb. Keep in mind a pip install for the appropriate adapter may be required as the current 'requirements.txt' only includes PyMySQL==0.9.3

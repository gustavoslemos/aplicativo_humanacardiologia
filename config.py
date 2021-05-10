import pyodbc 

DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = '*@@(@&#()&¨&341234214¨&8**#@!'

CORS_HEADERS = 'Content-Type'

SERVER = "humanacardiologia.database.windows.net" 
DB = "DBHumanaCardiologia" 
USER = "humanacardiologiaadmin" 
PWD = "Ecgmapaholter2021!" 


drivers = [item for item in pyodbc.drivers()] 
driver = drivers[-1]
# driver = "SQL+Server"

SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{USER}:{PWD}@{SERVER}/{DB}?driver={driver}"
# SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'


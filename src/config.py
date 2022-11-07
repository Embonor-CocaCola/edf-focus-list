import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


AUTH_LOGIN_URL = os.environ.get('AUTH_LOGIN_URL')
AUTH_USERNAME = os.environ.get('AUTH_USERNAME')
AUTH_PASSWORD = os.environ.get('AUTH_PASSWORD')
DB_CONNECTION_HOST = os.environ.get('DB_CONNECTION_HOST')
DB_CONNECTION_PORT = os.environ.get('DB_CONNECTION_PORT')
DB_CONNECTION_DB = os.environ.get('DB_CONNECTION_DB')
DB_CONNECTION_USER= os.environ.get('DB_CONNECTION_USER')
DB_CONNECTION_PASSWORD= os.environ.get('DB_CONNECTION_PASSWORD')

EDF_FOCUS_LIST_URL = os.environ.get('EDF_FOCUS_LIST_URL')

FILE_NAME = os.environ.get('FILE_NAME')

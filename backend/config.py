import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'data'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'change-this-development-secret')
    USERS_DB_PATH = os.path.join(DATA_DIR, 'users.csv')
    PORTFOLIO_DB_PATH = os.path.join(DATA_DIR, 'sample_data.csv')

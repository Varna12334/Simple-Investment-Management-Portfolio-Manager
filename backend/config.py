import os

class Config:
    # Secret key used for signing session cookies/tokens
    SECRET_KEY = os.environ.get('SECRET_KEY', 'super-secret-institutional-key-12345')
    
    # Path where user credentials are saved safely
    USERS_DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/users.csv'))

import os

class Config:
    SECRET_KEY = 'shhhhhh' 
    DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'forum.db')

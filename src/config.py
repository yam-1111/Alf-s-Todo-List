import os 

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'todo-app'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///todo.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
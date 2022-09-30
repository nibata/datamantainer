from distutils.debug import DEBUG
import os


basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URI')
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgrespw@localhost:55001/flask_app"

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "TO DREAM AN IMPOSSIBLE DREAM, TO FIGHT AN UNBEATABLE FOE, TO BEAR WITH UNBEARABLE SORROW, AND TO RUN WHERE THE BRAVE DARE NOT GO"

DEBUG = True
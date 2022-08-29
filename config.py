import os

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URI')

SQLALCHEMY_TRACK_MODIFICATIONS = True
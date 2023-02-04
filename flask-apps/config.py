import os
from dotenv import load_dotenv
from distutils.debug import DEBUG


# Cargo manualmente las variables de entorno. No se porqué en ocaciones funciona sin cargarlo y en otras no
load_dotenv()


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("FLASK_DEBUG")

REDIS_URL = os.environ.get("REDIS_URL")
 
BABEL_DEFAULT_LOCALE = os.environ.get("BABEL_DEFAULT_LOCALE")

DB_DRIVER = os.environ.get("DB_DRIVER")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")

SQLALCHEMY_DATABASE_URI = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

SENTRY_DSN = os.environ.get("SENTRY_DNS")
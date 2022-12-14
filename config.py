import os
from dotenv import load_dotenv
from distutils.debug import DEBUG


# Cargo manualmente las variables de entorno. No se porqué en ocaciones funciona sin cargarlo y en otras no
load_dotenv()


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI")

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("FLASK_DEBUG")

REDIS_URL = os.environ.get("REDIS_URL")
 
BABEL_DEFAULT_LOCALE = os.environ.get("BABEL_DEFAULT_LOCALE")
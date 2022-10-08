from distutils.debug import DEBUG
from dotenv import load_dotenv
import os


# Cargo manualmente las variables de entorno. No se porque en ocaciones funciona sin cargarlo y en otras no
load_dotenv()


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URI')

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "TO DREAM AN IMPOSSIBLE DREAM, TO FIGHT AN UNBEATABLE FOE, TO BEAR WITH UNBEARABLE SORROW, AND TO RUN WHERE THE BRAVE DARE NOT GO"

DEBUG = True
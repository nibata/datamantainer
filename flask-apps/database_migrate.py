from apps.app_test import app
from dotenv import load_dotenv
from flask_migrate import upgrade
from config import SQLALCHEMY_DATABASE_URI

load_dotenv()

if __name__ == '__main__':
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    with app.app_context():
        upgrade()

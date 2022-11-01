import email
import random
import sys
from faker import Faker
from apps.app_test.models.User import User
from config import SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


def create_fake_users(n, create_user_admin=True):
    """Generate fake users."""
    faker = Faker()
    for i in range(n):
        user = User(name=faker.first_name(),
                    age=random.randint(20, 80),
                    address=faker.address().replace('\n', ', '),
                    last_name=faker.last_name(),
                    email=faker.unique.email(),
                    password=User.set_password("pwd_test"))
        db.session.add(user)

    if create_user_admin:
        user_dummy = User(name="Nicolás",
                        age=33,
                        address="Holanda 434 depto 62 Providencia Santiago",
                        last_name="Bacquet",
                        email="admin@gmail.com",
                        password=User.set_password("a1b2-3"))
        db.session.add(user_dummy)

    db.session.commit()

    user_created = n + 1 if create_user_admin else n

    print(f'Se crean {user_created} registros de tabla User en base de datos.')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Ingresar el número de registros a ingresar en la tabla User.')
        sys.exit(1)
    create_fake_users(int(sys.argv[1]), False)
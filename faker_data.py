import email
import random
import sys
from faker import Faker
from apps.app_test.models.User import User
from apps.app_test.models.Group import Group
from config import SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


def create_fake_users(n, create_user_admin=True):
    """
    Genera usuarios aleatorios
    :param n : int, cantidad de usuarios a crear en base de datos.
    :param create_user_admin: boolean, si ademas de los n usuarios a crear se crea un usuario cin valores fijos y no aleatorios
    """
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

    print(f"Se crean {user_created} registros de tabla User en base de datos.")


def create_fake_roles():
    """
    Crea roles por defecto (default y admin)
    """
    role_default = Group(code="default",
                         description="Grupo de usuario creado por default.")

    role_admin = Group(code="admin",
                       description="Grupo de usuario para administradores de la aplicación.")

    db.session.add(role_default)
    db.session.add(role_admin)
    
    db.session.commit()

    print(f"Se crean los roles admin y defaul.")


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Ingresar el número de registros a ingresar en la tabla User.")
        sys.exit(1)
    print(sys.argv)
    #create_fake_users(int(sys.argv[1]), False)
    create_fake_roles()

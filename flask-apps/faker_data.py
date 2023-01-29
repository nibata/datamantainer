import sys
import random
from flask import Flask
from faker import Faker
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
from apps.app_test.models.User import User
from apps.app_test.models.Group import Group


load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


def create_fake_users(n: int, create_user_admin: bool=True):
    """Crea usuarios aleatorios en base de datos. Puede incluir un usuario por defecto 

    Parameters
    ----------
    n : int
        Cantidad de registros a insertar
    create_user_admin : bool, optional
        Si dentro de los usuarios a crear de crea el usuario admin@gmail.com con password a1b2-3, Por defecto True
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
    """Crea los roles asociados a la base de datos
    """

    role_default = Group(code="default",
                         description="Grupo de usuario creado por default.")

    role_admin = Group(code="admin",
                       description="Grupo de usuario para administradores de la aplicación.")

    db.session.add(role_default)
    db.session.add(role_admin)
    
    db.session.commit()

    print(f"Se crean los roles admin y defaul.")


def append_roles_to_users(consider_admin_user: bool=True):
    """A los usuarios creados se les asigna su rol

    Parameters
    ----------
    consider_admin_user : bool, optional
        Si al usario admin@gmail.com se le agrega el rol admin, by default True
    """

    db.engine.execute(
        """
            INSERT INTO authentication.users_groups(user_id, group_id) 
            SELECT id, (SELECT id FROM authentication.groups WHERE code = 'default')
            FROM authentication.users
        """
    )

    if consider_admin_user:
        db.engine.execute(
            """
               INSERT INTO authentication.users_groups(user_id, group_id) VALUES
                    ((SELECT id FROM authentication.users WHERE email='admin@gmail.com'),
                    (SELECT id FROM authentication.groups WHERE code = 'admin'))
            """
        )
    
    db.session.commit()

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Ingresar el número de registros a ingresar en la tabla User.")
        sys.exit(1)

    create_fake_roles()
    create_fake_users(n=int(sys.argv[1]), create_user_admin=True)
    append_roles_to_users(consider_admin_user=True)

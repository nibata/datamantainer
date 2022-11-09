import unittest
from ...app_test import app, db


class BaseTestClass(unittest.TestCase):
    def setUp(self):
        # self.app = create_app(settings_module="config.testing")
        self.app = app
        self.client = self.app.test_client()
        # Crea un contexto de aplicación
        with self.app.app_context():
            # TODO Ver cimo usar alembic en este punt
            # db.create_all()
            ...

    def tearDown(self):
        with self.app.app_context():
            # Elimina todas las tablas de la base de datos (Ver como usar alembic)
            # db.session.remove()
            # db.drop_all()
            ...

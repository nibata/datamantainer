from distutils.log import debug
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from services.database import db

from routes.user_bp import user_bp
from routes.group_bp import group_bp
from routes.default_bp import default_bp

from controllers.errors import page_not_found, server_error


# Aplicación
app = Flask(__name__)
app.config.from_object("config")

# Seguridad para formularios
csrf = CSRFProtect(app)

# Base de datos
db.init_app(app)
migrate = Migrate(app, db)

# Registro controladores
app.register_blueprint(default_bp, url_prefix="/")
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(group_bp, url_prefix="/groups")

# Páginas de error
app.register_error_handler(404, page_not_found)
app.register_error_handler(500, server_error)


if __name__ == "__main__":
    app.run()
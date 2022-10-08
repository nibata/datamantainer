from distutils.log import debug
from flask import Flask, render_template, url_for
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from services.database import db
from services.login_manager import login_manager

from routes.user_bp import user_bp
from routes.group_bp import group_bp
from routes.default_bp import default_bp
from routes.login_bp import login_bp

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
app.register_blueprint(login_bp, url_prefix="/login")

# Páginas de error
app.register_error_handler(404, page_not_found)
app.register_error_handler(500, server_error)


# Manejo de Sesiones login
login_manager.init_app(app)
#login_manager.login_view(url_for("login_bp.login"))


if __name__ == "__main__":
    app.run()

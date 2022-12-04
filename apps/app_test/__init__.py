from distutils.log import debug
from flask import Flask, request
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from .services.database import db
from .services.translate import babel
from .services.redis_service import redis_client
from .services.login_manager import login_manager

from .routes.user_bp import user_bp
from .routes.group_bp import group_bp
from .routes.login_bp import login_bp
from .routes.default_bp import default_bp

from .controllers.errors import page_not_found, server_error


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
app.register_blueprint(login_bp, url_prefix="/user_manager")

# Páginas de error
app.register_error_handler(404, page_not_found)
app.register_error_handler(500, server_error)


# Manejo de Sesiones login
login_manager.init_app(app)
login_manager.login_view = "/user_manager/login"

# Manejo de redis (variables almacendas en cache)
redis_client.init_app(app)

# Manejo de internacionalización

babel.init_app(app)

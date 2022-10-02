from distutils.log import debug
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from services.database import db

from routes.user_bp import user_bp
from routes.group_bp import group_bp


# Aplicación
app = Flask(__name__)
app.config.from_object("config")

# Seguridad para formularios
csrf = CSRFProtect(app)

# Base de datos
db.init_app(app)
migrate = Migrate(app, db)

# Registro controladores
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(group_bp, url_prefix='/groups')


@app.route('/')
def index():
    app.logger.info("HELLO WORLD!")
    return render_template('Views/default/index.html')


if __name__ == '__main__':
    app.run()

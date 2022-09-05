from flask import Flask, render_template
from flask_migrate import Migrate

from services.database import db

from routes.user_bp import user_bp
from routes.group_bp import group_bp


app = Flask(__name__)
app.config.from_object("config")


db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(group_bp, url_prefix='/groups')


@app.route('/')
def index():
    app.logger.info("HELLO WORLD!")
    return render_template('default/index.html')


if __name__ == '__main__':
    app.run()

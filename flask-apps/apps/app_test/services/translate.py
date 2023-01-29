from flask import request
from flask_babel import Babel, format_date, gettext


babel = Babel()


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(["en", "es"])

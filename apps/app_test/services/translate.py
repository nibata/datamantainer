from flask_babel import Babel, format_date, gettext
from flask import request


babel = Babel()


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(["en", "es"])


from werkzeug.middleware.dispatcher import DispatcherMiddleware
from app_test import app as app_test

application = DispatcherMiddleware(app_test, {"/app_test": app_test})
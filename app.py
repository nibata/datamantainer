from werkzeug.middleware.dispatcher import DispatcherMiddleware
from apps.app_test import app as app_test

application = DispatcherMiddleware(app_test, {"/app_test": app_test})
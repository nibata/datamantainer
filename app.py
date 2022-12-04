from apps.app_test import app as app_test
from werkzeug.middleware.dispatcher import DispatcherMiddleware

apps_pool = DispatcherMiddleware(app_test, {"/app_test": app_test})
from apps.app_test import create_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app_test = create_app()

# En el caso de que quisiera agregar más aplicaciones debería realizarlo acá, asignando 
# el path y la variable app de cada aplicación que se encuentra en el __init__.py
apps_pool = DispatcherMiddleware(app_test, {"/app_test": app_test})
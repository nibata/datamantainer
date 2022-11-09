# DataMantainer
Mantenedor de base de datos utilizando flask y postgres

Para correr la aplicacion se deben crear las siguiente variables de entorno (pueden ser configuradas mediante archivo `.env`):

 - **DB_URI**: contiene el string de conexión a base de datos
 - **SECRET_KEY**: llave secreta utilizada en los formularios en el uso de la librería csrf
 - **FLASK_APP**: script python que inicia el servidor si se desea iniciar el servidor mediante comando `flask run` (de momento solo logro hacerlo funcionar con aplicaciones individuales, para este caso `run_single_app.py`)

Para migraciones:

 - `flask db migrate -m "MENSAJE"`
 - `flask db updrade`

Con la base de datos creada se puede utilizar el script `faker_data.py` para crear datos de prueba. Por ejemplo si se queren crear 100 registros para la tabla user (tabla creada con los comandos de migración) de deje ejecutar el siguiente script:

`python faker_data.py 100`

Para ejecutar la aplicación:

 - `flask run` configurando la variable de entorn **FALSK_APP** a una aplicación individual
 - `python run.py` que corre multiples aplicaciones mediante `werkzeug.serving.run_simple` (por defecto está solamente expuesto a `127.0.0.1:5000`)
 - `gunicorn run:application -b 0.0.0.0` para ejecutar multiples aplicaciones mediante **GUNICORN**

Para ejecutar con docker-compose, dado que estoy utilizando postgres y procesador M1 es necesario ejecutar `export DOCKER_DEFAULT_PLATFORM=linux/amd64`

**Obs:** Desde el commit del 2022-11-09 se agregó la estructura necesaria para ejecutar *test unitarios* mediante la librería `unittest` de python por lo que ejecutar `python -m unittest` ejecuta los test unitarios. Esto está pensado para que cada aplicación tenga sus propios test unitarios.
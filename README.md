# DataMantainer
Mantenedor de base de datos utilizando flask y postgres

Para correr la aplicacion se deben crear las siguiente variables de entorno (pueden ser configuradas mediante archivo `.env`):

 - **DB_URI**: contiene el string de conexión a base de datos
 - **SECRET_KEY**: llave secreta utilizada en los formularios en el uso de la librería csrf
 - **FLASK_APP**: script python que inicia el servidor si se desea iniciar el servidor mediante comando `flask run`

Para migraciones:

 - `flask db migrate -m "MENSAJE"`
 - `flask db updrade`

Con la base de datos creada se puede utilizar el script `faker_data.py` para crear datos de prueba. Por ejemplo si se queren crear 100 registros para la tabla user (tabla creada con los comandos de migración) de deje ejecutar el siguiente script:

`python faker_data.py 100`
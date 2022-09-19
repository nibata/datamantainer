# DataMantainer
Mantenedor de base de datos utilizando flask y postgres

El string de conexión a la base de datos debe ser configurado como variable de ambiente (.env) con el nombre `DB_URI`

Para migraciones:

 - `flask db migrate -m "MENSAJE"`
 - `flask db updrade`
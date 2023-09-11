# Prueba base de datos usuario

install:

```
pip install SQLAlchemy
```

```
pip install psycopg2-binary
```

```
pip install alembic
```

Configurar la variable de entorno:

```
export DB_URI="postgresql://cwfvbvxl:jtsNDRjbVqGeBgYcYvxGps3LLlX_t-P5@berry.db.elephantsql.com:5432/cwfvbvxl"
```

Para aplicar la migracion:

```
alembic upgrade head
```

Para hacer una migración de la base de datos:

```
alembic revision --autogenerate -m "motivo de la migración"
```


Para hacer las consultas o modificaciones en models/users/queries.py 
hay algunas funciones que se importaron al main y se pueden usar desde ahi, 
esta todo comentado salvo la que imprime las filas de la tabla

```
python3 main.py
```





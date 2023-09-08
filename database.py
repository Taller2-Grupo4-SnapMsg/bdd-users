from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.users.model import User
from models.users.queries import *
from models.users.model import Base

#Esto es lo que iria en el backend para conectarme y tendria que ver como importar las funciones para utilizar la bdd

# Crear una conexión a la base de datos
engine = create_engine("postgresql://cwfvbvxl:jtsNDRjbVqGeBgYcYvxGps3LLlX_t-P5@berry.db.elephantsql.com:5432/cwfvbvxl")

# Crea las tablas en la base de datos (esto creará todas las tablas definidas en tus modelos)
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Crear un nuevo estudiante y agregarlo a la base de datos

#new_user = create_user(session, "marta00", "#pass00", "marta00@fi.uba.ar")
#new_user = create_user(session, "marta01", "#pass01", "marta01@fi.uba.ar")
#new_user = create_user(session, "marta02", "#pass02", "marta02@fi.uba.ar")
#new_user = create_user(session, "marta03", "#pass03", "marta03@fi.uba.ar")
#user_id = get_id_by_username(session, "marta02")
#delete_user(session, user_id)

# Consultar la base de datos para obtener todos los estudiantes
users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Username: {user.username}, Password: {user.password}, Email: {user.email}")

# Cerrar la sesión
session.close()
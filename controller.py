from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.users.model import User
from models.users.queries import *
from models.users.model import Base
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

#Esto es lo que iria en el backend para conectarme y tendria que ver como importar las funciones para utilizar la bdd

# Crear una conexión a la base de datos
engine = create_engine("postgresql://cwfvbvxl:jtsNDRjbVqGeBgYcYvxGps3LLlX_t-P5@berry.db.elephantsql.com:5432/cwfvbvxl")

# Crea las tablas en la base de datos (esto creará todas las tablas definidas en tus modelos)
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/users")
async def get_users():
    """
    Get all users
    """
    users = session.query(User).all()
    return users

# Define a Pydantic model for the request body
class UserRegistration(BaseModel):
    """
    This class is a Pydantic model for the request body.
    """

    password: str
    email: str
    nickname: str

@app.post("/register_new_user")
async def register_new_user(user: UserRegistration):
    """
    Register a new user
    """
    new_user = create_user(session, user.nickname, user.password, user.email)
    return new_user

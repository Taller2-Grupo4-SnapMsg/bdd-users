from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.users.model import User
from models.users.queries import get_user_by_username as get_user_by_username_db
from models.users.queries import get_user_by_id as get_user_by_id_db
from models.users.queries import delete_user as delete_user_db
from models.users.queries import get_user_by_mail as get_user_by_mail_db
from models.users.queries import create_user
from models.users.model import Base
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
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
    username: str = ''
    surname: str = ''
    name: str = ''
    password: str = ''
    email: str = ''
    date_of_birth: str = ''

@app.post("/register_new_user")
async def register_new_user(user: UserRegistration):
    """
    Register a new user

    Args:
        user (UserRegistration): The user to register.
    
    Returns:
        UserRegistration: The user that was registered.
    
    Raises:
        HTTPException: Returns a 400 Bad Request if the username or email already exists.
    """
    new_user = create_user(session,
                           user.username,
                           user.surname,
                           user.name,
                           user.password,
                           user.email,
                           user.date_of_birth)
    if new_user is None:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    return new_user

@app.delete("/delete_user")
async def delete_user(user_id: int):
    """
    Delete user
    """
    delete_user_db(session, user_id)

@app.get("/get_user_by_id")
async def get_user_by_id(user_id: int):
    """
    Obtener usuario por id
    """
    return get_user_by_id_db(session, user_id)

@app.get("/get_user_by_username")
async def get_user_by_username(username: str):
    """
    Gets user details by username.

    Args:
        username (str): The username of the user to retrieve.
    
    Returns:
        UserRegistration: User details.

    Raises:
        HTTPException: Returns a 400 Bad Request if the username does not exist.
    """
    user = get_user_by_username_db(session, username)
    if user is None:
        raise HTTPException(status_code=400, detail="Username does not exist")
    return user

@app.get("/get_user_by_mail", response_model=UserRegistration)
async def get_user_by_mail(mail: str):
    """
    Get user details by email.

    Args:
        mail (str): The email of the user to retrieve.

    Returns:
        UserResponseModel: User details.

    Raises:
        HTTPException: Returns a 400 Bad Request if the email does not exist.
    """
    user = get_user_by_mail_db(session, mail)
    if user is None:
        raise HTTPException(status_code=400, detail="Mail does not exist")
    return user

@app.delete("/delete_user_by_mail")
async def delete_user_by_mail(mail: str):
    """
    Delete user by email.
    """
    user = get_user_by_mail_db(session, mail)
    if user is None:
        raise HTTPException(status_code=400, detail="Mail does not exist")
    delete_user_db(session, user.id)

session.close()
from .model import User
from sqlalchemy.exc import IntegrityError

def get_user_by_id(session, user_id):
    return session.query(User).filter(User.id == user_id).first()

def get_user_by_username(session, username):
    return session.query(User).filter(User.username == username).first() #Por que first? deberia ser unico.

def get_user_by_mail(session, mail):
    return session.query(User).filter(User.email == mail).first()

def create_user(session, username, surname, name, password, email, date_of_birth):
    user = User(username=username, surname=surname, name=name, password=password,
                email=email, date_of_birth=date_of_birth)
    try:
        session.add(user)
        session.commit()
        return user
    except IntegrityError:
        session.rollback()
        return None
    
def update_user(session, user_id, new_data):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        for key, value in new_data.items():
            setattr(user, key, value)
        session.commit()
        return user
    return None

def delete_user(session, user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return True
    return False

def get_id_by_username(session, username):
    """ESTA MAL CONCEPTUALMENTE"""
    return session.query(User).filter(User.username == username).first().id
import database.entities.user as entities
import libs.hasher as hasher
from sqlalchemy.orm import Session


def get_username(id: int, session: Session):
    return session.get(entities.User, id).username


def is_user_with_email_exists(email: str, session: Session):
    return bool(session.query(entities.User).filter_by(email=email).first())


def create_new_user(email, username, password, session: Session):
    user = entities.User(email, username, hasher.hash_password(password))
    session.add(user)
    session.commit()


def auth(email: str, password: str, session: Session):
    user = session.query(entities.User).filter_by(email=email).first()
    if user:
        if hasher.compare(password, user.password):
            return user.id
        else:
            return False
    else:
        return False

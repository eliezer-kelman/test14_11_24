from consumers.db.models import User
from consumers.settings.conection_postgresql import get_session


def get_user_by_email(email):
    with get_session() as session:
        return session.query(User).filter(User.email == email).first()


def insert_user(new_user: User):
    with get_session() as session:
        user = get_user_by_email(new_user.email)
        if user:
            return
        session.add(new_user)
        session.commit()

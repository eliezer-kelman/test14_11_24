from consumers.db.models import FullMessage
from consumers.settings.conection_postgresql import get_session


def get_full_message_by_message_id(message):
    with get_session() as session:
        return session.query(FullMessage).filter(FullMessage.message == message).first()


def insert_full_message(new_full_message: FullMessage):
    with get_session() as session:
        session.add(new_full_message)
        session.commit()

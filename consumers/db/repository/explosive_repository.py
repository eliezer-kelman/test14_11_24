from consumers.settings.conection_postgresql import get_session


def insert_sentence_in_explosive(new_sentence):
    with get_session() as session:
        session.add(new_sentence)
        session.commit()

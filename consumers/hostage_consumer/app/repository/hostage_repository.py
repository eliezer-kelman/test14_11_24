from consumers.db.repository.full_message_repository import insert_full_message
from consumers.hostage_consumer.app.servise import convert_json_to_full_message


def insert_hostage(message):
    insert_full_message(convert_json_to_full_message(message))




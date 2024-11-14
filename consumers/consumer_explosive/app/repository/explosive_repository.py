from consumers.consumer_explosive.app.servise import convert_json_to_full_message
from consumers.db.repository.full_message_repository import insert_full_message


def insert_explosive(message):
    insert_full_message(convert_json_to_full_message(message.value))




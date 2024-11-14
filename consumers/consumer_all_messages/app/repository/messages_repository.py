from consumers.settings.conection_mongodb import get_all_messages_collection


def insert_message(message):
    member = get_all_messages_collection().insert_one(message.value)
    return member.inserted_id
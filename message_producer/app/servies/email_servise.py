import json
from typing import List
from message_producer.app.kafka_produser.all_message_producer import produce_all_message
from message_producer.app.kafka_produser.explos_producer import produce_explos_in_message
from message_producer.app.kafka_produser.hostage_producer import produce_hostage_in_message


def monitoring(email: json):
    produce_all_message(email)
    if is_explos(email['sentences']):
        produce_hostage_in_message(arrangement_of_a_message(email))
    elif is_hostage(email['sentences'])
        produce_explos_in_message(arrangement_of_a_message(email))


def is_explos(sentences: List) -> bool:
    for sentence in sentences:
        if 'explos' in sentence:
            return True
    return False

def is_hostage(sentences: List) -> bool:
    for sentence in sentences:
        if 'hostage' in sentence:
            return True
    return False

def arrangement_of_a_message(email: json) -> json:
    email['sentences'] = sorted(email['sentences'], key=lambda s: not ('explos' in s or 'hostage' in s))
    return email
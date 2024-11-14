import os
from dotenv import load_dotenv
from kafka_settings.producer import produce

load_dotenv(verbose=True)
topic_explosive = os.environ['TOPIC_EXPLOSIVE_MESSAGES_NAME']

def produce_explos_in_message(email_info):
    produce(
        topic=topic_explosive,
        key=email_info['email'],
        value=email_info)
import os
from dotenv import load_dotenv
from kafka_settings.producer import produce

load_dotenv(verbose=True)
topic_all_message = os.environ['TOPIC_ALL_MESSAGES_NAME']

def produce_all_message(email_info):
    produce(
        topic=topic_all_message,
        key=email_info['email'],
        value=email_info)
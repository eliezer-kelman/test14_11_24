import os
from dotenv import load_dotenv
from kafka_settings.producer import produce

load_dotenv(verbose=True)
topic_hostage = os.environ['TOPIC_HOSTAGE_MESSAGES_NAME']

def produce_hostage_in_message(email_info):
    produce(
        topic=topic_hostage,
        key=email_info['email'],
        value=email_info)
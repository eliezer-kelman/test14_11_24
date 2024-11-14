import os
from dotenv import load_dotenv
from kafka_settings.producer import produce

load_dotenv(verbose=True)
explosive_topic = os.environ['TOPIC_EXPLOSIVE_MESSAGES_NAME']

def produce_explos_in_message(email_info):
    produce(
        topic=explosive_topic,
        key=email_info['email'].encode('utf-8'),
        value=email_info)
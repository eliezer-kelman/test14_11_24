import os
from dotenv import load_dotenv
from kafka_settings.producer import produce

load_dotenv(verbose=True)
all_message_topic = os.environ['TOPIC_ALL_MESSAGES_NAME']

def produce_all_message(email_info):
    produce(
        topic=all_message_topic,
        key=email_info['email'].encode('utf-8'),
        value=email_info)
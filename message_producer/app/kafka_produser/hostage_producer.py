import os
from dotenv import load_dotenv
from kafka_settings.producer import produce

load_dotenv(verbose=True)
hostage_topic = os.environ['TOPIC_HOSTAGE_MESSAGES_NAME']

def produce_hostage_in_message(email_info):
    produce(
        topic=hostage_topic,
        key=email_info['email'].encode('utf-8'),
        value=email_info)
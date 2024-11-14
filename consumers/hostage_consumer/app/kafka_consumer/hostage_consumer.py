import os
from dotenv import load_dotenv
from kafka_settings.consumer import consume

load_dotenv(verbose=True)
topic_hostage = os.environ['TOPIC_HOSTAGE_MESSAGES_NAME']

def consume_hostage():
    consume(
        topic=topic_explosive,
        function=insert_hostage
    )
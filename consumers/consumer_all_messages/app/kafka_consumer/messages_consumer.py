import os
from dotenv import load_dotenv
from consumers.consumer_all_messages.app.repository.messages_repository import insert_message
from kafka_settings.consumer import consume

load_dotenv(verbose=True)
topic_all_message = os.environ['TOPIC_ALL_MESSAGES_NAME']

def consume_messages():
    consume(
        topic=topic_all_message,
        function=insert_message
    )
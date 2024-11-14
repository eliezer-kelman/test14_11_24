import os
from dotenv import load_dotenv
from consumers.consumer_all_messages.app.repository.messages_repository import insert_explosive
from kafka_settings.consumer import consume

load_dotenv(verbose=True)
topic_explosive = os.environ['TOPIC_EXPLOSIVE_MESSAGES_NAME']

def consume_explosive():
    consume(
        topic=topic_explosive,
        function=insert_explosive
    )
import json
import os
from typing import Callable, Any

from dotenv import load_dotenv
from kafka import KafkaConsumer

load_dotenv(verbose=True)

def consume(topic: str, function: Callable[[Any], Any] ,mode='latest'):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset=mode
    )
    for message in consumer:
        function(message)


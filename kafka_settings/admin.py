import os
from dotenv import load_dotenv
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError


load_dotenv(verbose=True)

def init_topics():
    client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
    all_message_topic = NewTopic(
        name=os.environ['TOPIC_ALL_MESSAGES_NAME'],
        num_partitions=int(os.environ['NUM_PARTITIONS']),
        replication_factor=int(os.environ['REPLICATION_FACTOR'])
    )
    hostage_topic = NewTopic(
        name=os.environ['TOPIC_HOSTAGE_MESSAGES_NAME'],
        num_partitions=int(os.environ['NUM_PARTITIONS']),
        replication_factor=int(os.environ['REPLICATION_FACTOR'])
    )
    explosive_topic = NewTopic(
        name=os.environ['TOPIC_EXPLOSIVE_MESSAGES_NAME'],
        num_partitions=int(os.environ['NUM_PARTITIONS']),
        replication_factor=int(os.environ['REPLICATION_FACTOR'])
    )
    try:
        client.create_topics([all_message_topic, hostage_topic, explosive_topic])
    except TopicAlreadyExistsError as e:
        print(e)
    finally:
        client.close()

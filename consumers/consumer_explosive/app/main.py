from consumers.consumer_explosive.app.kafka_consumer.explosive_consumer import consume_explosive
from consumers.settings.conection_postgresql import init_db

if __name__ == '__main__':
    init_db()
    consume_explosive()

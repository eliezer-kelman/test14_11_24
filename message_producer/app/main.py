from flask import Flask

from kafka_settings.admin import init_topics
from message_producer.app.routes.emails import emails_blueprint

app = Flask(__name__)
app.register_blueprint(emails_blueprint, url_prefix='/api')



if __name__ == '__main__':
    init_topics()
    app.run()
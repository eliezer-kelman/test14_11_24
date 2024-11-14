from flask import Blueprint, request, jsonify

from message_producer.app.servies.email_servise import monitoring

emails = Blueprint('emails', __name__)


@emails.route('/email', methods=['POST'])
def email_monitoring():
    data = request.json
    monitor = monitoring(data)
    return jsonify(data)
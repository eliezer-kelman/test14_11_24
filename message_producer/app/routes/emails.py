from flask import Blueprint, request, jsonify

from message_producer.app.servies.email_servise import monitoring

emails_blueprint = Blueprint('api', __name__)


@emails_blueprint.route('/email', methods=['POST'])
def email_monitoring():
    data = request.json
    monitoring(data)
    return jsonify('Received email'), 200
from flask import Blueprint, request, jsonify


emails = Blueprint('emails', __name__)


@emails.route('/email', methods=['POST'])
def email_monitoring():
    data = request.json
    print(data)
    return jsonify(data)
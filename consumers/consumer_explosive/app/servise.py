from enum import member

from pyexpat.errors import messages

from consumers.db.models import FullMessage, User, Location, Device, SuspiciousExplosiveContent


def convert_json_to_full_message(json_message) -> FullMessage:
    return FullMessage(
        user = User(
            username = json_message['username'],
            email = json_message['email'],
            ip_address = json_message['ip_address'],
            created_at = json_message['created_at']
        ),
        location = Location(
            latitude= json_message['location']['latitude'],
            longitude= json_message['location']['longitude'],
            city= json_message['location']['city'],
            country= json_message['location']['country']
        ),
        device_info = Device(
            device_id = json_message['device_info']['device_id'],
            os = json_message['device_info']['os'],
            browser = json_message['device_info']['browser']
        ),
        suspicious_explosive_content = SuspiciousExplosiveContent(
            message = json_message['sentences'][0]
        ),
        message = ', '.join(json_message['sentences'])
    )
from consumers.db.models import Device
from consumers.settings.conection_postgresql import get_session


def get_device_by_device_id(device_id):
    with get_session() as session:
        return session.query(Device).filter(Device.device_id == device_id).first()


def insert_device(new_device: Device):
    with get_session() as session:
        device = get_device_by_device_id(new_device.device_id)
        if device:
            return
        session.add(new_device)
        session.commit()

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from consumers.db.models import Base


class FullMessage(Base):
    __tablename__ = 'full_messages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    location_id = Column(Integer, ForeignKey('locations.id'))
    device_id = Column(Integer, ForeignKey('devices.id'))
    suspicious_hostage_content_id = Column(Integer, ForeignKey('suspicious_hostage_content.id'))
    suspicious_explosive_content_id = Column(Integer, ForeignKey('suspicious_explosive_content.id'))
    message = Column(String)


    user = relationship('User', back_populates='full_messages')
    location = relationship('Location', back_populates='full_messages')
    device = relationship('Device', back_populates='full_messages')
    suspicious_hostage_content = relationship('SuspiciousHostageContent', back_populates='full_message')
    suspicious_explosive_content = relationship('SuspiciousExplosiveContent', back_populates='full_message')

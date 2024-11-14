from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.models import Base


class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(String, unique=True)
    browser = Column(String)
    os = Column(String)

    full_messages = relationship('FullMessage', back_populates='device')
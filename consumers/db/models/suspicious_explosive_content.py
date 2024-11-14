from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.models import Base


class SuspiciousExplosiveContent(Base):
    __tablename__ = 'suspicious_explosive_content'
    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String, nullable=False)
    full_message_id = Column(String, ForeignKey('full_message.id'))

    full_message = relationship('FullMessage', back_populates='suspicious_explosive_content')
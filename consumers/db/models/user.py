from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from consumers.db.models import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    ip_address = Column(String(50), nullable=False)
    created_at = Column(String(50), nullable=False)

    # Relationships
    full_messages = relationship('FullMessage', back_populates='user')
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.models import Base


class User(Base):
    __tablename__ = 'users'

    country_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

    # Relationships
    full_messages = relationship('FullMessage', back_populates='user')
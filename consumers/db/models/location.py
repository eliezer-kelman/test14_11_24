from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.db.models import Base


class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)

    full_messages = relationship('FullMessage', back_populates='location')
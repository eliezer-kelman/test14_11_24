import os
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from consumers.db.models import Base

engine = create_engine('postgresql://admin:1234@172.24.255.254:5432/monitoring_messages')
session_maker = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

@contextmanager
def get_session():
    session = session_maker()
    try:
        yield session
    finally:
        session.close()


def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

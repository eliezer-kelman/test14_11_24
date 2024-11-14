import os
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://admin:1234@172.24.255.254:5432/monitoring_messages')
session_maker = sessionmaker(bind=engine)

@contextmanager
def get_session():
    session = session_maker()
    try:
        yield session
    finally:
        session.close()

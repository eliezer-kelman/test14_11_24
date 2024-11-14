import os
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(os.environ['POSTGRESQL_DB_URL'])
session_maker = sessionmaker(bind=engine)

@contextmanager
def get_session():
    session = session_maker()
    try:
        yield session
    finally:
        session.close()

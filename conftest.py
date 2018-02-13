import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_NAME = "testmigrations"


@pytest.fixture(scope="function")
def db_session():
    engine = create_engine('postgresql://postgres:postgres@localhost/{0}'.format(DB_NAME), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()

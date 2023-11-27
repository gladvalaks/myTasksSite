from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@127.0.0.1/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, isolation_level="REPEATABLE READ")
Session = sessionmaker(engine)
Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()

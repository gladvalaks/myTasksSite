from sqlalchemy import Integer, String, Column

from database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    email = Column(String(), nullable=False)
    username = Column(String(), nullable=False)
    password = Column(String(), nullable=False)

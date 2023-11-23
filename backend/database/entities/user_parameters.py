from sqlalchemy import Integer, String, Column, ForeignKey
from uuid import uuid4
from database.database import Base


class UserParameters(Base):
    __tablename__ = "user_parameters"

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("users.id"))
    user_coins_required = Column(Integer(), default=10)
    user_token = Column(String(), default=uuid4())

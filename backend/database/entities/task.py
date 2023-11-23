from datetime import datetime
from sqlalchemy import Integer, String, Text, Boolean, Column, DateTime, ForeignKey

from database.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    description = Column(Text())
    coins = Column(Integer(), nullable=False)
    user_id = Column(Integer(), ForeignKey("users.id"))
    is_daily = Column(Boolean(), default=False)
    task_priority_id = Column(Integer(), ForeignKey("task_priorities.id"))
    created_at = Column(DateTime(), default=datetime.now())
    finished_at = Column(DateTime())

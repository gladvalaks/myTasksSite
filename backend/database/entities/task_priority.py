from database.database import Base
from sqlalchemy import Integer, String, Column


class TaskPriority(Base):
    __tablename__ = "task_priorities"

    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    order = Column(Integer(), nullable=False)

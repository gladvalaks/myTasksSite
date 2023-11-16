from sqlalchemy.orm import Session 

import database.entities.task_priority as entities
from models.responses.task_priority import TaskPriority


def create_task_priority(title: str, order: int, session: Session):
    session.add(entities.TaskPriority(title=title, order=order))
    session.commit()


def get_serialized_priorities(session: Session):
    serialized_priorities = [
        TaskPriority(**serialize(priority))
        for priority in session.query(entities.TaskPriority).all()
    ]
    return serialized_priorities


def serialize(task_priority):
    return {
        "id": task_priority.id,
        "title": task_priority.title,
        "order": task_priority.order,
    }

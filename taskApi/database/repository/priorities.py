import database.entities.task_priority as entities
import database.database as db
import models.responses.task_priority as task_priority_response
from sqlalchemy.orm import Session

def create_task_priority(title, order,session:Session):
    task_priority = entities.TaskPriority(title, order)
    session.add(task_priority)
    session.commit()

def get_serialized_priority(priority):
    return priority.serialize()

def get_serialized_priorities(session:Session):
    priorities = session.query(entities.TaskPriority).all()
    serialized_priorities = [get_serialized_priority(priority) for priority in priorities]
    return serialized_priorities

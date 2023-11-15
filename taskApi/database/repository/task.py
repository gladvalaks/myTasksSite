import database.entities.task as entities
import database.database as db
import models.responses.task as task_response
from sqlalchemy.orm import Session
import datetime

def create_task(title, coins, user_id, is_daily, task_priority_id, description, session:Session):
    task = entities.Task(title, coins, user_id, is_daily, task_priority_id, description)
    session.add(task)
    session.commit()

def delete_task(id,session:Session):
    task = session.get(entities.Task,id)
    session.delete(task)
    session.commit()

def edit_task(id, title, coins, is_daily, task_priority_id, description,session:Session):
    task = session.get(entities.Task,id)
    task.edit(title, coins, is_daily, task_priority_id, description)
    session.commit()

def complete_task(id,session:Session):
    task = session.get(entities.Task,id)
    if(task.is_daily):
        create_task(*task.get_values(),session)
    task.complete()
    session.commit()



def get_serialized_today_tasks(user_id,session:Session):
    tasks = session.query(entities.Task).filter_by(user_id=user_id).all()
    today = datetime.datetime.now().date()
    serialized_tasks = []
    for task in tasks:
        if(task.finished_at is not None and task.finished_at.date() != today ):
            continue
        serialized_tasks.append(task.get_full_info())       
    return serialized_tasks

def get_serialized_tasks(user_id,session:Session):
    tasks = session.query(entities.Task).filter_by(user_id=user_id).all()
    serialized_tasks = [task.get_full_info() for task in tasks]
    return serialized_tasks


def is_user_task(user_id, task_id,session:Session):
    task = session.get(entities.Task,task_id)
    return user_id == task.user_id
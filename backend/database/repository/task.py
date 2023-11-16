from sqlalchemy.orm import Session
import datetime

import database.entities.task as entities

def create_task(
    title: str,
    coins: int,
    user_id: int,
    is_daily: bool,
    task_priority_id: int,
    description: str,
    session: Session,
):
    task = entities.Task(
        title=title,
        coins=coins,
        user_id=user_id,
        is_daily=is_daily,
        task_priority_id=task_priority_id,
        description=description,
    )
    session.add(task)
    session.commit()


def delete_task(id: int, session: Session):
    task = session.get(entities.Task, id)
    session.delete(task)
    session.commit()


def edit_task(
    id: int,
    title: str,
    coins: int,
    is_daily: bool,
    task_priority_id: int,
    description: str,
    session: Session,
):
    task = session.get(entities.Task, id)
    task.title = title
    task.coins = coins
    task.is_daily = is_daily
    task.task_priority_id = task_priority_id
    task.description = description
    session.commit()


def complete_task(id: int, session: Session):
    task = session.get(entities.Task, id)
    if task.is_daily:
        print(get_values(task))
        create_task(*   get_values(task), session)
    task.finished_at = datetime.datetime.now()
    session.commit()

def uncomplete_task(id: int, session: Session):
    task = session.get(entities.Task, id)
    task.finished_at = None
    session.commit()

def get_serialized_today_tasks(user_id: int, session: Session):
    tasks = session.query(entities.Task).filter_by(user_id=user_id).all()
    today = datetime.datetime.now().date()
    serialized_tasks = []
    for task in tasks:
        if task.finished_at is not None and task.finished_at.date() != today:
            continue
        serialized_tasks.append(serialize(task))
    return serialized_tasks


def get_serialized_tasks(user_id: int, session: Session):
    tasks = session.query(entities.Task).filter_by(user_id=user_id).all()
    serialized_tasks = [serialize(task) for task in tasks]
    return serialized_tasks


def is_user_task(user_id: int, task_id: int, session: Session):
    task = session.get(entities.Task, task_id)
    return user_id == task.user_id


def get_values(task: entities.Task):
    return [
        task.title,
        task.coins,
        task.user_id,
        task.is_daily,
        task.task_priority_id,
        task.description,
    ]


def serialize(task: entities.Task):
    finished_at = task.finished_at
    if finished_at:
        finished_at = int(round(finished_at.timestamp() * 1000))
    return {
        "id": task.id,
        "title": task.title,
        "coins": task.coins,
        "user_id": task.user_id,
        "is_daily": task.is_daily,
        "task_priority_id": task.task_priority_id,
        "description": task.description,
        "created_at": int(round(task.created_at.timestamp() * 1000)),
        "finished_at": finished_at,
    }

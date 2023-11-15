from fastapi import Response, status, APIRouter, Depends
from typing import Annotated
from database.database import get_session
from sqlalchemy.orm import Session
import models.requests.task as task_requests_models
import database.repository.task as task_repo
import libs.token as jwt_token

router = APIRouter()


@router.get("/api/tasks")
def get_tasks(
    response: Response,
    user_id: Annotated[int, Depends(jwt_token.get_user_id)],
    session: Session = Depends(get_session),
):
    try:
        response.status_code = status.HTTP_200_OK
        return task_repo.get_serialized_today_tasks(user_id, session)

    except Exception as er:
        return {"response": "fail"}


@router.post("/api/tasks")
def create_task(
    task_body: task_requests_models.TaskBody,
    response: Response,
    user_id: Annotated[int, Depends(jwt_token.get_user_id)],
    session: Session = Depends(get_session),
):
    task_repo.create_task(
        task_body.title,
        task_body.coins,
        user_id,
        task_body.is_daily,
        task_body.task_priority_id,
        task_body.description,
        session,
    )
    response.status_code = status.HTTP_201_CREATED


@router.delete("/api/tasks/{task_id}")
def delete_task(
    task_id: int,
    user_id: Annotated[int, Depends(jwt_token.get_user_id)],
    session: Session = Depends(get_session),
):
    if task_repo.is_user_task(user_id, task_id, session):
        task_repo.delete_task(task_id, session)
        return {"response": "task was deleted"}
    return {"response": "You don't have the rights to do this"}


@router.put("/api/tasks/{task_id}")
def edit_task(
    task_id: int,
    task_body: task_requests_models.TaskBody,
    response: Response,
    user_id: Annotated[int, Depends(jwt_token.get_user_id)],
    session: Session = Depends(get_session),
):
    if task_repo.is_user_task(user_id, task_id, session):
        task_repo.edit_task(
            task_id,
            task_body.title,
            task_body.coins,
            task_body.is_daily,
            task_body.task_priority_id,
            task_body.description,
            session,
        )
        response.status_code = status.HTTP_202_ACCEPTED
        return {"response": "task_is_edited"}


@router.patch("/api/tasks/{task_id}/complete")
def complete_task(
    task_id: int,
    response: Response,
    user_id: Annotated[int, Depends(jwt_token.get_user_id)],
    session: Session = Depends(get_session),
):
    if task_repo.is_user_task(user_id, task_id, session):
        task_repo.complete_task(task_id, session)
        response.status_code = status.HTTP_202_ACCEPTED
        return {"response": "task_is_complete"}
    response.status_code = status.HTTP_403_FORBIDDEN
    return {"response": "You don't have the rights to do this"}

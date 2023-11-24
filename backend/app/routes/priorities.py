from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_session
import database.repository.priorities as priorities_repo

router = APIRouter()


@router.get("/api/priorities")
def get_priorities(session: Session = Depends(get_session)):
    return priorities_repo.get_serialized_priorities(session)
@router.get("/api/priorities/HI")
def HI():
    return "HI"
from fastapi import APIRouter, Depends
from database.database import get_session
from sqlalchemy.orm import Session
import database.repository.priorities as priorities_repo

router = APIRouter()


@router.get("/api/priorities")
def get_priorities(session: Session = Depends(get_session)):
    return priorities_repo.get_serialized_priorities(session)

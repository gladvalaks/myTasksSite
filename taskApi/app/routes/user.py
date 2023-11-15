from fastapi import  Response, Request,status
from fastapi import APIRouter,Depends
from database.database import get_session
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi.responses import JSONResponse
import models.requests.user as models
import database.repository.user as db
import app.token as token

router = APIRouter()


@router.post("/api/auth")
def auth(user:models.UserForAuth, response:Response,session:Session = Depends(get_session)):
    user_id = db.auth(user.email, user.password,session)  
    if user_id:
        res = JSONResponse(content={"response": "OK"})
        res.set_cookie(
            key="token",
            value=token.create_access_token(data={"user_id": user_id}),
            secure=False,
            samesite=None,
        )
        response.status_code = status.HTTP_200_OK
        return res
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED


@router.post("/api/register")
def register(user_data: models.UserForRegistration, response:Response,session:Session = Depends(get_session)):
    try:
        if db.is_user_with_email_exists(user_data.email,session):
            response.status_code = status.HTTP_409_CONFLICT
            return {"response": "This email already is used"}
        db.create_new_user(user_data.email, user_data.username, user_data.password,session)
        response.status_code = status.HTTP_201_CREATED
        return {"response": "OK"}
    except Exception as er:
        print(er)
        return {"response": "fail"}
    
@router.get("/api/user")
def get_name(response:Response,user_id: Annotated[int,Depends(token.get_user_id)],session:Session = Depends(get_session)):
    response.status_code = status.HTTP_200_OK
    return db.get_username(user_id,session)

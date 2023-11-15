from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Cookie,Depends,Response
from typing import Annotated
import database.repository.user  as db

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def delete_token():
    response = Response()
    response.delete_cookie("token")

def decrypt_access_token(token: Annotated[str, Cookie()]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
    except Exception as err:
        print("Сломався")
        delete_token()
        return 0
    return user_id

def get_user_id(user_id: Annotated[int,Depends(decrypt_access_token)]):
    return user_id


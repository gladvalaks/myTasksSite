from fastapi import FastAPI
from pydantic import BaseModel
import Database as db
from Hasher import*

class UserDataForRegistration(BaseModel):
    email: str
    username: str
    password: str

class UserDataForAuth(BaseModel):
    email:str
    password:str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "fghhrld"}

@app.post("/auth")
def auth(user_data: UserDataForAuth):
    try:
        pass
    except:
        pass


@app.post("/register")
def register(user_data :UserDataForRegistration):
    try:
        db.create_new_user(user_data.email,user_data.username,user_data.password)
        return {"response":"OK"}
    except Exception as er:
        print(er)
        return {"response":"fail"}
        
    
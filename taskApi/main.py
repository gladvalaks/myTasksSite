from fastapi import FastAPI
from pydantic import BaseModel
import Database as db
from Hasher import*

class UserDataForRegistration(BaseModel):
    email: str
    username: str
    password: str

class TaskBody(BaseModel):
    title: str
    description:str
    coins:int
    user_id: int
    is_daily: bool
    task_priority_id: int

class UserDataForAuth(BaseModel):
    email:str
    password:str

class GetTasks(BaseModel):
    user_id:int

app = FastAPI()

@app.get("/tasks")
def get_taks(get_tasks:GetTasks):
    try:
        return db.get_tasks(get_tasks.user_id)
    except Exception as er:
        print(er)
        return{"response":"fail"}

@app.post('/tasks')
def create_task(task_body:TaskBody):
    db.create_task(task_body.title,task_body.coins,
                   task_body.user_id,task_body.is_daily,
                   task_body.task_priority_id,task_body.description
                   )

@app.get("/priorities")
def get_priorities():
    return db.get_priorities()

@app.post("/auth")
def auth(user_data: UserDataForAuth):
    try:
        pass
    except:
        pass


@app.post("/register")
def register(user_data :UserDataForRegistration):
    try:
        if(db.check_user_by_email(user_data.email)):
            return {"response": "This email already is used"}
        db.create_new_user(user_data.email,user_data.username,user_data.password)
        return {"response":"OK"}
    except Exception as er:
        print(er)
        return {"response":"fail"}
        
    
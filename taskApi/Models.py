from pydantic import BaseModel

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

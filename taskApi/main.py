from fastapi import FastAPI
import Models
import Database as db
from Hasher import*




app = FastAPI()


@app.get("/tasks")
def get_taks(get_tasks:Models.GetTasks):
    try:
        return db.get_tasks(get_tasks.user_id)
    except Exception as er:
        print(er)
        return{"response":"fail"}

@app.post('/tasks')
def create_task(task_body:Models.TaskBody):
    db.create_task(task_body.title,task_body.coins,
                   task_body.user_id,task_body.is_daily,
                   task_body.task_priority_id,task_body.description
                   )
    
@app.put('/tasks/{task_id}')
def edit_task(task_id:int, task_body:Models.TaskBody):
    db.edit_task(task_id,task_body.title,task_body.coins,
                task_body.is_daily, task_body.task_priority_id,
                task_body.description
                )

@app.patch('/tasks/{task_id}/complete')
def complete_task(task_id:int):
    db.complete_task(task_id)

@app.get("/priorities")
def get_priorities():
    return db.get_priorities()



@app.post("/auth")
def auth(user_data: Models.UserDataForAuth):
    try:
        pass
    except:
        pass


@app.post("/register")
def register(user_data :Models.UserDataForRegistration):
    try:
        if(db.check_user_by_email(user_data.email)):
            return {"response": "This email already is used"}
        db.create_new_user(user_data.email,user_data.username,user_data.password)
        return {"response":"OK"}
    except Exception as er:
        print(er)
        return {"response":"fail"}
        
    
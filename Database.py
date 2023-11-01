from sqlalchemy import create_engine, insert, MetaData, Table, Integer, String, Text, Column, DateTime, ForeignKey, Numeric, CheckConstraint,Boolean
from datetime import datetime
from Hasher import *

engine = create_engine('sqlite:///database.db') 
metadata = MetaData()
conn = engine.connect()

User = Table('users', metadata, 
    Column('id', Integer(), primary_key=True),
    Column('email',String(),nullable=False),
    Column('username',String(),nullable=False),
    Column('password',String(),nullable=False)
    )
TaskPriority = Table('task_priority',metadata,
    Column('id',Integer(),primary_key=True),
    Column('title',String(),nullable= False),
    Column('order',Integer(),nullable=False)
    )
Task = Table('tasks',metadata,
    Column('id',Integer(),primary_key=True),
    Column('title',String(),nullable=False),
    Column('description',Text()),
    Column('coins',Integer()),
    Column('user_id',ForeignKey('users.id')),
        Column('is_daily',Boolean,default=False),
        Column('task_priority',ForeignKey('task_priority.id')),
        Column('created_at',DateTime(),default=datetime.now()),
        Column('finished_at',DateTime())
        )

metadata.create_all(engine)

def create_new_user(username,email,password):
    new_user = User.insert().values(
        email = email,
        username = username,
        password = Hasher.hash_password(password)
    )
    conn = engine.connect()
    conn.execute(new_user)
    conn.commit()

def auth(email,password):
    pass


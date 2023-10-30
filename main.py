# main.py
from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a sqlite engine instance
engine = create_engine("sqlite:///mytodo.db")

# Create a DeclarativeMeta instance
Base = declarative_base()

# Define To Do class inheriting from Base
class ToDo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task =  Column(String(50))

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/todo")
def create_todo():
    return "create todo item"

@app.get("/todo/{id}")
def read_todo(id: int):
    return "read todo item with id {id}"

@app.put("/todo/{id}")
def update_todo(id: int):
    return "update todo item with id {id}"

@app.delete("/todo/{id}")
def delete_todo(id: int):
    return "delete todo item with id {id}"

@app.get("/todo")
def read_todo_list():
    return "read todo list"
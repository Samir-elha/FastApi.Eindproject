from fastapi import FastAPI, status, HTTPException
from .database import Base, engine, ToDo
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

# DATABASE_URL = "sqlite:///./sqlite.db"

# Create ToDoRequest Base Model
class ToDoRequest(BaseModel):
    task: str

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost",
    "https://samir-elha.github.io/samir3.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return "todooo"

@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo(todo: ToDoRequest):

    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # create an instance of the ToDo database model
    tododb = ToDo(task = todo.task)

    # add it to the session and commit it
    session.add(tododb)
    session.commit()

    # grab the id given to the object from the database
    id = tododb.id

    # close the session
    session.close()

    # return the id
    return f"created todo item with id {id}"

@app.get("/todo/{id}")
def read_todo(id: int):
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)
    # get the todo item with the given id
    todo = session.query(ToDo).get(id)
    # close the session
    session.close()
    try:
        return f"todo item with id: {todo.id} and task: {todo.task}"
    except AttributeError:
        return "todo item not found"

@app.put("/todo/{id}")
def update_todo(id: int, task: str):

    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the todo item with the given id
    todo = session.query(ToDo).get(id)

    # update todo item with the given task (if an item with the given id was found)
    if todo:
        todo.task = task
        session.commit()

    # close the session
    session.close()

    # check if todo item with given id exists. If not, raise exception and return 404 not found response
    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo

@app.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id: int):

    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the todo item with the given id
    todo = session.query(ToDo).get(id)

    # if todo item with given id exists, delete it from the database. Otherwise raise 404 error
    if todo:
        session.delete(todo)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return None

@app.get("/todo")
def read_todo_list():
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get all todo items
    todo_list = session.query(ToDo).all()

    # close the session
    session.close()

    return todo_list
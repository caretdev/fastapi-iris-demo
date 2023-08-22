from fastapi import FastAPI, Depends
from .db import init_db, get_session
from . import crud, schemas

app = FastAPI(
    title='TODO Application',
    version='1.0.0',
)


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/todo", response_model=list[schemas.Todo])
async def read_todos(skip: int = 0, limit: int = 100, session=Depends(get_session)):
    todos = crud.get_todos(session, skip=skip, limit=limit)
    return todos


@app.post("/todo", response_model=schemas.Todo)
async def create_todo(todo: schemas.TodoCreate, session=Depends(get_session)):
    return crud.create_todo(db=session, todo=todo)

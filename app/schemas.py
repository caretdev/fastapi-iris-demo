from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    description: str


class Todo(TodoCreate):
    id: int

    class Config:
        from_attributes = True

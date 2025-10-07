from enum import IntEnum
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

api = FastAPI()
 
class Priority(IntEnum):
    lOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Name of the todo")
    description: str = Field(..., description="Description of the todo")
    priority: Priority = Field(default=Priority.lOW, description="Priority of the todo")

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int = Field(..., description="Unique identifier of the todo")

class TodoUpdate(TodoBase):
    name: Optional[str] = Field(None, min_length=3, max_length=50, description="Name of the todo")
    description: Optional[str] = Field(None, description="Description of the todo")
    priority: Optional[Priority] = Field(None, description="Priority of the todo")




all_todos = [
    Todo(id=1, name="Sports", description="Go to gym", priority=Priority.HIGH),
    Todo(id=2, name="Study", description="Read a book", priority=Priority.MEDIUM),
    Todo(id=3, name="Work", description="Complete the project", priority=Priority.lOW),
    Todo(id=4, name="Shopping", description="Buy groceries", priority=Priority.MEDIUM),
    Todo(id=5, name="Travel", description="Plan a trip", priority=Priority.lOW)
]

@api.get("/")
def index():
    return {"message": "Hello World"}

@api.get("/todos/{id}", response_model=Optional[Todo])
def get_todo(id: int):
    for todo in all_todos:
        if todo.id == id:
            return todo
    return None

@api.get("/todos", response_model=List[Todo])
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
    
@api.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    next_id = max((t.id for t in all_todos), default=0) + 1
    new_todo = Todo(id=next_id, **todo.dict())
    all_todos.append(new_todo)
    return new_todo

@api.put("/todos/{id}", response_model=Optional[Todo])
def update_todo(id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.id == id:
            if updated_todo.name:
                todo.name = updated_todo.name
            if updated_todo.description:
                todo.description = updated_todo.description
            if updated_todo.priority:
                todo.priority = updated_todo.priority
            return todo
    return None

@api.delete("/todos/{id}", response_model=Optional[Todo])
def delete_todo(id: int):
    for index, todo in enumerate(all_todos):
        if todo.id == id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    return None
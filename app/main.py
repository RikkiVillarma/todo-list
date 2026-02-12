from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Simple To-Do API")

class TodoItem(BaseModel):
    id: int
    task: str
    completed: bool

todos: List[TodoItem] = []

@app.get("/todos", response_model=List[TodoItem])
def get_todos():
    return todos

@app.post("/todos", response_model=TodoItem)
def add_todo(item: TodoItem):
    todos.append(item)
    return item

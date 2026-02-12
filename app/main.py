from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can later restrict to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

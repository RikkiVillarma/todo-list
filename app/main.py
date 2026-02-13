from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Simple To-Do API")

# -------------------------
# CORS middleware
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can later restrict to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Data models
# -------------------------
class TodoItem(BaseModel):
    id: int
    task: str
    completed: bool = False  # Default to False

# -------------------------
# In-memory storage
# -------------------------
todos: List[TodoItem] = []

# -------------------------
# Routes
# -------------------------

# Get all todos
@app.get("/todos", response_model=List[TodoItem])
def get_todos():
    return todos

# Add a new todo
@app.post("/todos", response_model=TodoItem)
def add_todo(item: TodoItem):
    item.id = len(todos) + 1  # Auto-increment ID
    todos.append(item)
    return item

# Update a todo (mark completed or edit task)
@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo(todo_id: int, updated_item: TodoItem):
    for todo in todos:
        if todo.id == todo_id:
            todo.task = updated_item.task
            todo.completed = updated_item.completed
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# Delete a todo
@app.delete("/todos/{todo_id}", response_model=dict)
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(i)
            return {"message": f"Todo {todo_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")

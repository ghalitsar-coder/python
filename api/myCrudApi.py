from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Initialize the FastAPI app
app = FastAPI()

# Define a model for a "To-Do" item
class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

# In-memory database (list) for storing to-do items
todo_list: List[Todo] = []

# Create a new to-do item
@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo):
    # Check for duplicate ID
    for existing_todo in todo_list:
        if existing_todo.id == todo.id:
            raise HTTPException(status_code=400, detail="ID already exists.")
    todo_list.append(todo)
    return todo

# Read all to-do items
@app.get("/todos/", response_model=List[Todo])
def get_all_todos():
    return todo_list

# Read a single to-do item by ID
@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo_by_id(todo_id: int):
    for todo in todo_list:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="To-Do item not found.")

# Update a to-do item by ID
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="To-Do item not found.")

# Delete a to-do item by ID
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            del todo_list[index]
            return {"message": "To-Do item deleted successfully."}
    raise HTTPException(status_code=404, detail="To-Do item not found.")

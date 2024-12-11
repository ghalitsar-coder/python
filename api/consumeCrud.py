import requests

# The base URL of the FastAPI app
BASE_URL = "http://127.0.0.1:8000"

# 1. Create a new to-do item (POST request)
def create_todo():
    url = f"{BASE_URL}/todos/"
    todo_data = {
        "id": 1,
        "title": "Learn FastAPI",
        "description": "Study FastAPI and create a CRUD API",
        "completed": False
    }
    
    response = requests.post(url, json=todo_data)
    if response.status_code == 200:
        print("Created To-Do:", response.json())
    else:
        print(f"Error: {response.status_code}, {response.text}")

# 2. Get all to-do items (GET request)
def get_all_todos():
    url = f"{BASE_URL}/todos/"
    response = requests.get(url)
    if response.status_code == 200:
        print("All To-Dos:", response.json())
    else:
        print(f"Error: {response.status_code}, {response.text}")

# 3. Get a to-do item by ID (GET request)
def get_todo_by_id(todo_id):
    url = f"{BASE_URL}/todos/{todo_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"To-Do {todo_id}:", response.json())
    else:
        print(f"Error: {response.status_code}, {response.text}")

# 4. Update a to-do item (PUT request)
def update_todo():
    url = f"{BASE_URL}/todos/1"
    updated_data = {
        "id": 1,
        "title": "Master FastAPI",
        "description": "Become an expert at building APIs",
        "completed": True
    }
    
    response = requests.put(url, json=updated_data)
    if response.status_code == 200:
        print("Updated To-Do:", response.json())
    else:
        print(f"Error: {response.status_code}, {response.text}")

# 5. Delete a to-do item (DELETE request)
def delete_todo():
    url = f"{BASE_URL}/todos/1"
    response = requests.delete(url)
    if response.status_code == 200:
        print("Deleted To-Do successfully.")
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    create_todo()    # Create a new to-do
    get_all_todos()  # Get all to-do items
    get_todo_by_id(1)  # Get a specific to-do by ID
    update_todo()    # Update a to-do item
    delete_todo()    # Delete a to-do item

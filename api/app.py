from fastapi import FastAPI

# Create FastAPI app
app = FastAPI()

# Define an endpoint
@app.get("/myapi")
def my_custom_api():
    return {"message": "Welcome to my custom API!", "author": "Your Name", "version": "1.0"}

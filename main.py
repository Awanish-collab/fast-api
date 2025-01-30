from fastapi import FastAPI

# Create a FastAPI instance
app = FastAPI()

@app.get("/")
def index():
    return {"message": "Welcome to FastAPI!"}

@app.get("/about")
def about():
    return {"info": "This is the About page."}
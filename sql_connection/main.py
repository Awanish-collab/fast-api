from fastapi import FastAPI
import models
from database import engine
from routers import blog, users, auth

app = FastAPI()

app.include_router(blog.router)

app.include_router(users.router)

app.include_router(auth.router)

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def blog_get():
    return {"message": "Blog Successfully Created"}



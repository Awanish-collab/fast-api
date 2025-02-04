from sqlalchemy.orm import Session
import models
from schemas import Blog
from fastapi import HTTPException, status

def blog_get_response(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def get_by_id(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog not available for the given id {id}.")
    return blog

def create(request: Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with give id {id}, not available.")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"Message": "Given blog id {id}, Successfully deleted."}

def update(id: int, request, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with give id {id}, not available.")
    blog.update(request.model_dump())
    db.commit()
    return "Updated"
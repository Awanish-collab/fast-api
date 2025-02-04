from fastapi import APIRouter, Depends, HTTPException, status, Response
from typing import List
from schemas import ShowBlog, Blog, User
import models
from sqlalchemy.orm import Session
from database import get_db
from repository import blog
from oauth2 import get_current_user

router = APIRouter(
    prefix="/blogs",
    tags=['Blogs']
)

#@router.get("/blog", response_model = List[ShowBlog])
@router.get("/", response_model = List[ShowBlog])  # prefix we added that's why we removed "blog" kept only "/"
def blog_get_response(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.blog_get_response(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def blog_post(request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    #return {"title": request.title, "body": request.body}
    return blog.create(request, db)
    

@router.get("/{id}", response_model=ShowBlog)
def blog_get_response(id: int, response: Response, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    '''blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"detail": f"Blog not available for the given id {id}."}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog not available for the given id {id}.")
    return blog'''
    return blog.get_by_id(id, db)
    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.destroy(id, db)



@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.update(id, request, db)
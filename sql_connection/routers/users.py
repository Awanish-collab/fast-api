from fastapi import APIRouter, Depends, HTTPException, status, Response
from typing import List
from sqlalchemy.orm import Session
from database import get_db
import models
from schemas import ShowUser, User
from repository import users

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

# creating user
@router.post("/")
def create_user(request: User, db: Session = Depends(get_db)):
    return users.create(request, db)


# display all users
#@router.get("/users", response_model = List[ShowUser], tags=['Users']) 
@router.get("/", response_model = List[ShowUser]) 
# because of this  response_model = List[ShowUser], id and password both are hided
def get_users(db: Session = Depends(get_db)):
    return users.get_all_users(db)

# display a specific user by id
#@router.get("/users/{id}", response_model = ShowUser) 
@router.get("/{id}", response_model = ShowUser) 
# giving "/{id}" because we added prefix into that otherwise need to give "/users/{id}"
# because of this  response_model = List[ShowUser], id and password both are hided
def get_users(id: int, db: Session = Depends(get_db)):
    return users.get_users_by_id(id, db)
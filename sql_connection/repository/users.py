from sqlalchemy.orm import Session
from get_hash import Hash
import models
from fastapi import HTTPException, status

def create(request, db: Session):
    hashed_password = Hash.encrypt_password(request.password)
    new_user = models.Users(name = request.name, email = request.email, password = hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db:Session):
    users = db.query(models.Users).all()
    return users

def get_users_by_id(id: int, db: Session):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not available for the given id {id}.")
    return user
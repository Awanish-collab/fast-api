from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config:
        orm_mode = True
        # orm_mode = True, FastAPI can convert ORM models into Pydantic models seamlessly.


# Creating  pydantic schema to Create user
class User(BaseModel):
    name: str
    email: str
    password: str    


class ShowUser(BaseModel):
    name: str
    email: str
    # In models.py, see we given blogs = relationship("Blog", back_populates="creator"), 
    # that's why need to give blogs field name
    blogs: List['Blog'] = []

    class Config:
        orm_mode = True


# we can define this showblog like both 2 ways, in first I used inheritance to extend the feature,
# BUT Suppose, if i want to display on title then we need to go with 2nd way, simply just give titl: str, remove the body: str
'''class ShowBlog(Blog):
    pass'''

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser   # this used to display user by help of foreign key and primary key

    class Config:
        orm_mode = True



class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
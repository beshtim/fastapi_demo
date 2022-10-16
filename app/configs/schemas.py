from typing import List, Union
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    psw: str

class UserShow(BaseModel):
    name: str
    email: str
    blogs: List[Blog] 
    class Config:
        orm_mode = True

class ShowBlog(BaseModel): # class ShowBlog(Blog):
    title: str
    body: str 
    creator: UserShow
    class Config:
        orm_mode = True

class Login(BaseModel):
    email: str
    psw: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None
from typing import List
from pydantic import BaseModel, EmailStr


class UserOut(BaseModel):
    id: int
    username: str


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    phone_number: str
    job: str
    gender: str
    password: str


class User(BaseModel):
    id: int
    username: str

    class config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int


class Command(BaseModel):
    command: str


class UserProfile(BaseModel):
    username: str
    gender: str
    job: str
    email: EmailStr
    phone_number: str

    class config:
        orm_mode = True
        
        
class GalleryContent(BaseModel):
    image_prompt: str
    image: str
    
    class config:
        orm_mode = True
        
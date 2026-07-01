from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Base schema jo user se data receive karega
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    #rating: Optional[int] = None

# Create ke liye schema (jo Base se sab kuch inherit kar raha hai)
class PostCreate(PostBase):
    pass

class UserCreate(BaseModel):
    email : EmailStr
    password : str

class UserOut(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime
    class Config:
        from_attributes = True
class UserLogin(BaseModel):
    email : EmailStr
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None

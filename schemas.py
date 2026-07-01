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

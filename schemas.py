from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from pydantic.types import conint
from typing import Optional

# 1. UserOut ko pehle rakhein taaki Post model isse use kar sake
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

# 2. Base class
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

# 3. Post model (PostOut se upar hona chahiye)
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    model_config = ConfigDict(from_attributes=True)

# 4. PostOut (Ab 'Post' yahan accessible hai)
class PostOut(BaseModel):
    Post: Post
    votes: int  

    model_config = ConfigDict(from_attributes=True)

# Baki models
class PostCreate(PostBase):
    pass

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

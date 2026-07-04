from fastapi import FastAPI, status, HTTPException, Response, Depends
from sqlalchemy.orm import Session
from . import models, schemas, utilis
from .database import engine, get_db
from .routers import post,user,auth, vote
from .config import settings

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

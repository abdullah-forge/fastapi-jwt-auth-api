from fastapi import FastAPI, status, HTTPException, Response, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas
from .. import utilis
from .. import schemas
from . import oauth2
from ..database import engine, get_db

router = APIRouter(
    prefix = "/posts",
    tags=['Post']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostBase)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    new_post = models.Post(**post.model_dump())
    db.add(new_post)

    db.commit()
    db.refresh(new_post)
    return new_post
    

@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}  

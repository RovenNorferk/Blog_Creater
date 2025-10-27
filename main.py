from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Annotated, Optional
from datetime import datetime 
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI(title="Blog API")  # Added title for better OpenAPI docs

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for local testing; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(bind=engine)

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class UserBase(BaseModel):
    username: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def home():
    return {'This is a Blog Creation Platform'}

@app.post("/posts/", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostBase, db: db_dependency):
    db_post = models.Post(**post.dict(exclude={"created_at", "updated_at"}))
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@app.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def read_post(post_id: int, db: db_dependency):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail='Post was not found')
    return post

@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int, db: db_dependency):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post was not found')
    db.delete(db_post)
    db.commit()

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict(exclude={"created_at", "updated_at"}))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user
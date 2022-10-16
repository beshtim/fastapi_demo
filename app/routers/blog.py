from fastapi import APIRouter, Depends, status, Response, HTTPException
from ..configs import schemas, models
from ..configs.database import get_db
from ..configs.oauth2 import get_current_user
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

@router.get("", response_model=List[schemas.Blog])
def get_all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.get("/{id}", status_code=200, response_model=schemas.Blog)
def get_one(id, response: Response, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"{id} is not in the db"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} is not in the db")
    return blog

@router.post("", status_code=status.HTTP_201_CREATED)
def create(req: schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=req.title, body=req.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db:Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="wrong id")
    blog.delete(synchronize_session=False)
    db.commit()
    return "done"

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def upd(id, req: schemas.Blog, db:Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="wrong id")
    blog.update(req)
    db.commit()
    return 'updated'



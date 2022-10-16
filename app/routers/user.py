from fastapi import APIRouter, Depends, status, Response, HTTPException
from ..configs import schemas, models, hashing
from ..configs.database import get_db
from sqlalchemy.orm import Session
from ..configs.oauth2 import get_current_user


router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("", response_model=schemas.UserShow)
def create_user(req: schemas.User, db:Session = Depends(get_db)):
    new_user = models.User(name=req.name, email=req.email, psw=hashing.Hash.encrypt(req.psw))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return req

@router.get("/{id}", status_code=200, response_model=schemas.UserShow)
def get_one_user(id, response: Response, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} is not in the db")
    return user 
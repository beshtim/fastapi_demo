from fastapi import APIRouter, Depends, status, Response, HTTPException
from ..configs import schemas, models, hashing, JWTtoken
from ..configs.database import get_db
from typing import List
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/login',
    tags=["login"]
)

@router.post("")
def login(req: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == req.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid credintials")
    if not hashing.Hash.verify(user.psw, req.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid password")
    
    access_token = JWTtoken.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
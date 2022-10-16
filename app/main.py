from fastapi import FastAPI
from .configs.database import engine
from .configs import models

from .routers import blog, user, login

app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(login.router)

models.Base.metadata.create_all(bind=engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/blog", status_code=status.HTTP_201_CREATED, tags=["blog"])
# def create(req: schemas.Blog, db:Session = Depends(get_db)):
#     new_blog = models.Blog(title=req.title, body=req.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog 

# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["blog"])
# def delete_blog(id, db:Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="wrong id")
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return "done"

# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["blog"])
# def upd(id, req: schemas.Blog, db:Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="wrong id")
#     blog.update(req)
#     db.commit()
#     return 'updated'

# @app.get("/blog", response_model=List[schemas.Blog], tags=["blog"])
# def get_all(db:Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get("/blog/{id}", status_code=200, response_model=schemas.Blog, tags=["blog"])
# def get_one(id, response: Response, db:Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"detail": f"{id} is not in the db"}
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} is not in the db")
#     return blog


# @app.post("/user", response_model=schemas.UserShow, tags=["user"])
# def create_user(req: schemas.User, db:Session = Depends(get_db)):
#     new_user = models.User(name=req.name, email=req.email, psw=hashing.Hash.encrypt(req.psw))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return req

# @app.get("/user/{id}", status_code=200, response_model=schemas.UserShow,tags=["user"])
# def get_one_user(id, response: Response, db:Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} is not in the db")
#     return user
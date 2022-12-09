from fastapi import FastAPI, Request,Depends,HTTPException,Response,File, UploadFile
from pydantic import BaseModel
import  schemas,models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import re 
import pdftotext
import os
import parser
from pymongo import MongoClient

client=MongoClient('localhost',27017)
mondo_db=client['resume']


app = FastAPI()

api_key="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"

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# fastapi route for signup
@app.post("/signup")
def signup(request: schemas.SignupRequest, db: Session = Depends(get_db)):
    new_user = models.User(name=request.username, password=request.password, email=request.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # return a response
    return {"status": "success"}

# fastapi route for login
@app.post("/login",status_code=200)
def login(request: schemas.LoginRequest, db: Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.password == request.password:
        return {"message": "Invalid credentials"}


    # return a response
    return {"auth_token": "token"}


# fastapi route for getall users
@app.get("/getall")
def getall(db: Session = Depends(get_db)):
    # do something with the request
    users = db.query(models.User).all()
    # return a response
    return users

# update the user
@app.post("/updateprofile")
def updatprofile(request: schemas.User, db: Session = Depends(get_db)):
    # do something with the request
    user = db.query(models.User).filter(models.User.email==request.email).first()
    user.name=request.fullname
    user.email=request.email
    user.phone=request.phone
    db.commit()
    db.refresh(user)
    # return a response
    return {"status": "success"}


# route to upload a pdf
@app.post("/uploadfile{email}")
async def create_upload_file(email,file: UploadFile = File(...)):
    # do something with the request
    file_name = file.filename
    file_contents = await file.read()
    with open(file_name, "wb") as buffer:
        buffer.write(file_contents)
    # remove the file
    r=parser.ResumeParser(api_key)
    result=r.query_resume(pdf_path=file_name,email=email)
    # add the result in mongodb
    # monod_db.resume.insert_one(result)

    os.remove(file_name)
   

    # return a response
    return {"filename": result}


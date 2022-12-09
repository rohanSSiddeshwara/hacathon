from pydantic import BaseModel
from fastapi import File, UploadFile



# pydantic model for signup request
class SignupRequest(BaseModel):
    username: str
    password: str
    email: str

# pydantic model for login request
class LoginRequest(BaseModel):
    email: str
    password: str

class User(BaseModel):
    id: int
    fullname: str
    password: str
    email: str
    phone: str




    
    
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: str
    password: str

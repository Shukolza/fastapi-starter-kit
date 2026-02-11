from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    # username: str # change depending on what you use as the first factor
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    username: str

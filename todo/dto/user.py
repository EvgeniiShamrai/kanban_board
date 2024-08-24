import datetime

from pydantic import BaseModel
from pydantic import EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    role_id: int
    create_at: datetime.datetime
    updated_at: datetime.datetime

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    role_id: int
    password: str

class UserResponse(User):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: EmailStr | None = None
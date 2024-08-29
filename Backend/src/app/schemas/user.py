from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    name: str | None
    email: EmailStr| None
    phone : str| None

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserResponse(UserBase):
    id: int| None
    #created_at: datetime



class Users(BaseModel):
    data: list[UserResponse]

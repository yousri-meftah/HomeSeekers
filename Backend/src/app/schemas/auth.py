from pydantic import BaseModel
from typing import Optional


class UserLogin(BaseModel):
    email: str
    password: str
class register_return(BaseModel):
    status: str
    message: str

class Token(BaseModel):
    access_token: str
    token_type: str

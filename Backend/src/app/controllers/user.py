from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
from ..models import User
from ..services.auth import hash_password , verify_password, create_access_token
from ..schemas.user import UserCreate
from ..schemas.auth import UserLogin
from fastapi.security import OAuth2PasswordRequestForm
from app.exceptions.user import UserNotFoundException
from app.exceptions.user import UserEmailAlreadyExistsException


def register_user(user: UserCreate, db: Session):
    if db.query(User).filter(User.email == user.email).first():
        raise UserEmailAlreadyExistsException

    hashed_password = hash_password(user.password)
    db_user = User(
        name=user.name,
        email=user.email,
        phone=user.phone,
        password=hashed_password
    )
    db.add(db_user)


def authenticate_user(user_login: OAuth2PasswordRequestForm, db: Session):
    user = db.query(User).filter(User.email == user_login.username).first()
    if not user:
        raise UserNotFoundException

    if not verify_password(user_login.password, user.password):
        raise UserNotFoundException

    access_token = create_access_token(data={"sub": user.id})

    return {"access_token": access_token, "token_type": "bearer"}



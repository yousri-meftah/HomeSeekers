
from fastapi import Depends
from starlette.authentication import AuthCredentials, UnauthenticatedUser
from database import get_db
from sqlalchemy.orm import Session
from app.services.auth import decode_access_token
from fastapi.security import OAuth2PasswordBearer
from app.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")



def get_current_user(token: str = Depends(oauth2_scheme), db : Session = Depends(get_db)):
    payload = decode_access_token(token)
    if not payload or type(payload) is not dict:
        return None

    user_id = payload.get("id", None)
    if not user_id:
        return None

    id = int(user_id)

    user = db.query(User).filter(User.id == id).first()
    return user


class JWTAuth:
    async def authenticate(self, conn):
        guest = AuthCredentials(["unauthenticated"]), UnauthenticatedUser()
        if "authorization" not in conn.headers:
            return guest

        token = conn.headers.get("authorization").split(" ")[1]
        if not token:
            return guest

        user = get_current_user(token=token)
        if not user:
            return guest

        return AuthCredentials("authenticated"), user


from sqlalchemy.orm import Session
from redis import Redis
from app.models import Home
from app.schemas.home import HomeCreate, HomeUpdate
from app.exceptions.base import NotFoundException

def create_home(home_data: HomeCreate, db: Session, redis: Redis):
    new_home = Home(**home_data.dict(), owner_id=1)  # Assuming user_id is 1 for simplicity
    db.add(new_home)
    db.commit()
    db.refresh(new_home)
    redis.set(f"home_{new_home.id}", new_home)
    return new_home

def get_home(home_id: int, db: Session, redis: Redis):
    cached_home = redis.get(f"home_{home_id}")
    if cached_home:
        return cached_home
    home = db.query(Home).filter(Home.id == home_id).first()
    if not home:
        raise NotFoundException(detail="Home not found")
    redis.set(f"home_{home.id}", home)
    return home

def update_home(home_id: int, home_data: HomeUpdate, db: Session, redis: Redis):
    home = db.query(Home).filter(Home.id == home_id).first()
    if not home:
        raise NotFoundException(detail="Home not found")

    for key, value in home_data.dict(exclude_unset=True).items():
        setattr(home, key, value)

    db.commit()
    db.refresh(home)
    redis.set(f"home_{home.id}", home)
    return home

def delete_home(home_id: int, db: Session, redis: Redis):
    home = db.query(Home).filter(Home.id == home_id).first()
    if not home:
        raise NotFoundException(detail="Home not found")

    db.delete(home)
    db.commit()
    redis.delete(f"home_{home.id}")

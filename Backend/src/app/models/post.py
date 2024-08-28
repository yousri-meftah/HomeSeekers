from sqlalchemy import Column, Integer, String, Text, DECIMAL, Date, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from . import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"),nullable=False)
    home_id = Column(Integer, ForeignKey("homes.id"),nullable=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(DECIMAL(10, 2), nullable=False)
    post_date = Column(Date, server_default=func.current_date())
    is_active = Column(Boolean, server_default="true")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="posts")
    home = relationship("Home", back_populates="posts")
    images = relationship("ListingImage", back_populates="post")
    comments = relationship("Comment", back_populates="post")

from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from . import Base

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    contract_id = Column(Integer, ForeignKey("contracts.id"), nullable=False)
    notification_date = Column(DateTime(timezone=True), server_default=func.now())
    message = Column(Text, nullable=False)

    user = relationship("User", back_populates="notifications")
    contract = relationship("Contract", back_populates="notifications")

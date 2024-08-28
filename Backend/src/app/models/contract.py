from sqlalchemy import Column, Integer, Date, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from . import Base

class Contract(Base):
    __tablename__ = "contracts"
    id = Column(Integer, primary_key=True, index=True)
    home_id = Column(Integer, ForeignKey("homes.id"), nullable=False)
    renter_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    rent_amount = Column(DECIMAL(10, 2), nullable=False)
    payment_due_date = Column(Date, nullable=False)
    annual_increase_percentage = Column(DECIMAL(5, 2), nullable=False)
    deposit_amount = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    home = relationship("Home", back_populates="contracts")
    renter = relationship("User", back_populates="contracts_as_renter")
    payments = relationship("Payment", back_populates="contract")
    notifications = relationship("Notification", back_populates="contract")

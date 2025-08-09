
# models.py
from sqlalchemy import Column, Integer, String, Float, Boolean, Time, Text, DateTime
from sqlalchemy.sql import func
from .database import Base

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    cuisine_type = Column(String(50), nullable=False)
    address = Column(String(200), nullable=False)
    phone_number = Column(String(20), nullable=False)
    rating = Column(Float, default=0.0)
    is_active = Column(Boolean, default=True)
    opening_time = Column(Time, nullable=True)
    closing_time = Column(Time, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=True, default=func.now(), onupdate=func.now())

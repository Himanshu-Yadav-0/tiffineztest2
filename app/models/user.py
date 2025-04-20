from sqlalchemy import Column, String, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import enum
import uuid
from sqlalchemy.orm import relationship

from app.db.database import Base

class UserType(str, enum.Enum):
    customer = "CUSTOMER"
    owner = "OWNER"
    delivery = "DELIVERY"
    admin = "ADMIN"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    user_type = Column(Enum(UserType), nullable=False)
    location = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    
    services = relationship("TiffinService", back_populates="owner")
    subscriptions = relationship("Subscription", back_populates="user")

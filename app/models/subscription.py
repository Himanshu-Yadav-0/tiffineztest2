from sqlalchemy import Column, String, Date, Boolean, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.db.database import Base

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    service_id = Column(UUID(as_uuid=True), ForeignKey("tiffin_services.id"), nullable=False)
    total_tiffins = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    loan_allowed = Column(Boolean, default=False)
    default_meal_mode = Column(String, nullable=False)  # 'delivery' or 'dine_in'

    user = relationship("User", back_populates="subscriptions")
    service = relationship("TiffinService", back_populates="subscriptions")

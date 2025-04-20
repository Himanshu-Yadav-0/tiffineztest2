from sqlalchemy import Column, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base
import enum
from sqlalchemy.dialects.postgresql import UUID
import uuid


class MealType(str, enum.Enum):
    lunch = "lunch"
    dinner = "dinner"

class DailyMealMenu(Base):
    __tablename__ = "daily_meal_menu"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    service_id = Column(UUID(as_uuid=True), ForeignKey("tiffin_services.id"), nullable=False)
    date = Column(Date, nullable=False)
    meal_type = Column(Enum(MealType), nullable=False)
    items = Column(String, nullable=False)

    tiffin_service = relationship("TiffinService", back_populates="menus")

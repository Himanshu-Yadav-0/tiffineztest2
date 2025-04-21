from sqlalchemy import String, Column,  Date, Enum, ForeignKey,Boolean,Time,Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models import user,subscription
import uuid,enum
from app.db.database import Base

class MealType(enum.Enum):
    LUNCH = "lunch"
    DINNER = "dinner"


class Rating:
    __tablename__ = "Meal_Rating"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    service_id = Column(UUID(as_uuid=True),ForeignKey("tiffin_services.id"),nullable=False)
    date = Column(Date,nullable=False)
    meal_type = Column(Enum(MealType),nullable=False)
    rating = Column(Integer,default=0)
    review = Column(String)


from sqlalchemy import String, Column,  Date, Enum, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.user import User
from app.models.subscription import Subscription
import uuid,enum
from app.db.database import Base

class MealType(str, enum.Enum):
    lunch = "lunch"
    dinner = "dinner"


class User_meal_selection(Base):
    __tablename__ = "meal_selection"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    subscription_id = Column(UUID(as_uuid=True),ForeignKey("subscriptions.id"),nullable=False)
    date = Column(Date,nullable=False)
    meal_type = Column(Enum(MealType),nullable=False)
    opted_in =Column(Boolean,default=True)


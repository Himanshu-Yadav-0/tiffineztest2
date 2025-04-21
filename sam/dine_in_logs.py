from sqlalchemy import String, Column,  Date, Enum, ForeignKey,Boolean,Time
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models import user,subscription
import uuid,enum
from app.db.database import Base

class MealType(enum.Enum):
    LUNCH = "lunch"
    DINNER = "dinner"


class Dine_in(Base):
    __tablename__ = "dine_in"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    subscription_id = Column(UUID(as_uuid=True),ForeignKey("subscriptions.id"),nullable=False)
    date = Column(Date,nullable=False)
    meal_type = Column(Enum(MealType),nullable=False)
    scanned_at = Column(Time,nullable=False)
    verified = Column(Boolean,default=True)



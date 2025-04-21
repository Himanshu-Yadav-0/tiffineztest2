from sqlalchemy import String, Column,  Date, Enum, ForeignKey,Boolean,Time,Integer
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models import user,subscription
import uuid,enum
from app.db.database import Base

class MealType(enum.Enum):
    LUNCH = "lunch"
    DINNER = "dinner"


class Loans(Base):
    __tablename__ = "loans"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    subscription_id = Column(UUID(as_uuid=True),ForeignKey("subscriptions.id"),nullable=False)
    date = Column(Date,nullable=False)
    meal_type = Column(Enum(MealType),nullable=False)
    quantity = Column(Integer,default=0)
    settled = Column(Boolean,default=False)


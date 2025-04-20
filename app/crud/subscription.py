from app.models.subscription import Subscription
from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.subscription import SubscriptionCreate

def create_subscription(db: Session, user_id: UUID, sub_data: SubscriptionCreate):
    new_sub = Subscription(
        user_id=user_id,
        service_id=sub_data.service_id,
        total_tiffins=sub_data.total_tiffins,
        start_date=sub_data.start_date,
        end_date=sub_data.end_date,
        loan_allowed=sub_data.loan_allowed,
        default_meal_mode=sub_data.default_meal_mode
    )
    db.add(new_sub)
    db.commit()
    db.refresh(new_sub)
    return new_sub

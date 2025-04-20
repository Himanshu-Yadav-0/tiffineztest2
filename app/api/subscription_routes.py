from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.subscription import SubscriptionCreate, SubscriptionOut
from app.db.database import get_db
from app.utils.auth import get_current_user
from app.models.user import UserType, User
from app.crud.subscription import create_subscription

router = APIRouter()

@router.post("/", response_model=SubscriptionOut)
def subscribe_user(
    sub_data: SubscriptionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.user_type != UserType.customer:
        raise HTTPException(status_code=403, detail="Only customers can subscribe.")
    return create_subscription(db, current_user.id, sub_data)

from pydantic import BaseModel
from uuid import UUID
from datetime import date

class SubscriptionCreate(BaseModel):
    service_id: UUID
    total_tiffins: int
    start_date: date
    end_date: date
    loan_allowed: bool = False
    default_meal_mode: str  # 'delivery' or 'dine_in'

class SubscriptionOut(BaseModel):
    id: UUID
    service_id: UUID
    total_tiffins: int
    start_date: date
    end_date: date
    loan_allowed: bool
    default_meal_mode: str

    class Config:
        orm_mode = True

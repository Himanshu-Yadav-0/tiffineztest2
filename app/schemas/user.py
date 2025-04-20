from pydantic import BaseModel, constr
from typing import Optional
from uuid import UUID
from datetime import datetime
from enum import Enum

class UserType(str, Enum):
    customer = "CUSTOMER"
    owner = "OWNER"
    delivery = "DELIVERY"
    admin = "ADMIN"

class UserCreate(BaseModel):
    name: str
    phone: constr(min_length=10, max_length=15)
    password: str
    user_type: UserType
    location: Optional[str]

class UserOut(BaseModel):
    id: UUID
    name: str
    phone: str
    user_type: UserType
    created_at: datetime

    class Config:
        from_attributes = True

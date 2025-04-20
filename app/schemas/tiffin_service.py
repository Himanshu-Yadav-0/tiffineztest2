from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class TiffinServiceCreate(BaseModel):
    name: str
    description: str
    location: str

class TiffinServiceOut(TiffinServiceCreate):
    id: UUID
    owner_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True

class TiffinServiceOut(BaseModel):
    id: UUID
    name: str
    description: str
    location: str
    owner_id: UUID

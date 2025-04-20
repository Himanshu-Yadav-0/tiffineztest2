from sqlalchemy.orm import Session
from app.models.tiffin_service import TiffinService
from uuid import UUID

def get_service_by_owner(db: Session, owner_id: UUID):
    return db.query(TiffinService).filter(TiffinService.owner_id == owner_id).first()
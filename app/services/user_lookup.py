from sqlalchemy.orm import Session
from app.models.user import User

def get_user_by_phone(db: Session, phone: str):
    return db.query(User).filter(User.phone == phone).first()

from app.models.daily_menu import DailyMealMenu
from app.schemas.daily_menu import DailyMenuCreate
from sqlalchemy.orm import Session
import uuid

def create_menu(db: Session, service_id: str, data: DailyMenuCreate):
    menu = DailyMealMenu(
        id=str(uuid.uuid4()),
        service_id=service_id,
        date=data.date,
        meal_type=data.meal_type,
        items=data.items
    )
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return menu

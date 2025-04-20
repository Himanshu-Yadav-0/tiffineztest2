from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.tiffin_service import TiffinServiceCreate, TiffinServiceOut
from app.db.database import get_db
from app.utils.auth import get_current_user
from app.models.user import User,UserType
from app.models.tiffin_service import TiffinService
from app.schemas.daily_menu import DailyMenuCreate
from app.models.daily_menu import DailyMealMenu
from app.crud.daily_menu import create_menu
from app.crud.tiffin_service import get_service_by_owner



router = APIRouter(prefix="/tiffin-services", tags=["Tiffin Services"])

@router.post("/create", response_model=TiffinServiceOut)
def create_service(service: TiffinServiceCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    print(current_user.user_type)
    print(UserType.__members__)

    if current_user.user_type != UserType.owner:
        raise HTTPException(status_code=403, detail="Only owners can create tiffin services")

    new_service = TiffinService(
        name=service.name,
        description=service.description,
        location=service.location,
        owner_id=current_user.id
    )
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service

@router.post("/daily-menu")
def create_daily_menu(
    menu_data: DailyMenuCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.user_type != UserType.owner:
        raise HTTPException(status_code=403, detail="Only owners can add menu.")

    # 👇 Auto-fetch owner’s service
    service = get_service_by_owner(db, current_user.id)
    if not service:
        raise HTTPException(status_code=404, detail="Tiffin service not found for this owner.")

    menu = DailyMealMenu(
        service_id=service.id,
        date=menu_data.date,
        meal_type=menu_data.meal_type,
        items=menu_data.items
    )
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return menu

@router.get("/tiffin-services/mine", response_model=TiffinServiceOut)
def get_my_service(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.user_type != UserType.owner:
        raise HTTPException(status_code=403, detail="Only owners can access this route")

    service = get_service_by_owner(db, current_user.id)

    if not service:
        raise HTTPException(status_code=404, detail="No service found for this owner")

    return service


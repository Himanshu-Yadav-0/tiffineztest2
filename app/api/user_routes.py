from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.crud.user import create_user,get_user_by_phone
from app.db.database import SessionLocal
from fastapi.security import OAuth2PasswordRequestForm
from app.utils.auth import verify_password, create_access_token
from app.schemas.token import Token
from app.utils.auth import get_current_user



router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    from app.crud.user import get_user_by_phone
    if get_user_by_phone(db, user.phone):
        raise HTTPException(status_code=400, detail="Phone already registered")
    return create_user(db, user)

@router.post("/login", response_model=Token)
def login_user(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_phone(db, data.username)
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(data={"sub": user.phone, "role": user.user_type})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut)
def read_current_user(current_user = Depends(get_current_user)):
    return current_user
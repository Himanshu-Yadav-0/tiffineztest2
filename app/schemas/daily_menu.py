from pydantic import BaseModel
from datetime import date
from enum import Enum

class MealType(str, Enum):
    lunch = "lunch"
    dinner = "dinner"

class DailyMenuCreate(BaseModel):
    date: date
    meal_type: MealType
    items: str


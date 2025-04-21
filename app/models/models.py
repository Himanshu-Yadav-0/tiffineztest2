from sqlalchemy import String, Column,  Date, Enum, ForeignKey,Boolean,Integer,Time,JSON,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from models.user import User
from models.subscription import Subscription
import uuid,enum
from db.database import Base

class MealType(str, enum.Enum):
    lunch = "lunch"
    dinner = "dinner"

class UserType(str, enum.Enum):
    customer = "CUSTOMER"
    owner = "OWNER"
    delivery = "DELIVERY"
    admin = "ADMIN"
#USER
class User(Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    user_type = Column(Enum(UserType), nullable=False)
    location = Column(String, nullable=False)
    created_at = Column(Date,nullable= False)


# Define the TiffinService model
class TiffinService(Base):
    __tablename__ = 'tiffin_services'

    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    name = Column(String)
    description = Column(String)
    location = Column(String)
    owner_id = Column(String)

#SUBSCRIPTION
class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)  # Assuming 'id' is a string (e.g., 'SUB1', 'SUB2')
    user_id = Column(String, nullable=False)
    service_id = Column(String, nullable=False)
    total_tiffins = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    loan_allowed = Column(Boolean, nullable=False)
    default_meal_mode = Column(String, nullable=False)


class TempDeliveryRequest(Base):
    __tablename__ = 'temp_delivery_requests'

    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    user_id = Column(String, nullable=False)
    service_id = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    meal_type = Column(String, nullable=False)

class User_meal_selection(Base):
    __tablename__ = "meal_selection"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    subscription_id = Column(UUID(as_uuid=True),ForeignKey("subscriptions.id"),nullable=False)
    date = Column(Date,nullable=False)
    meal_type = Column(Enum(MealType),nullable=False)
    opted_in =Column(Boolean,default=True)


class Rating:
    __tablename__ = "Meal_Rating"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    service_id = Column(UUID(as_uuid=True),ForeignKey("tiffin_services.id"),nullable=False)
    date = Column(Date,nullable=False)
    meal_type = Column(Enum(MealType),nullable=False)
    rating = Column(Integer,default=0)
    review = Column(String)

class Loans(Base):
    __tablename__ = "loans"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    subscription_id = Column(UUID(as_uuid=True),ForeignKey("subscriptions.id"),nullable=False)
    date = Column(Date,nullable=False)
    meal_type = Column(Enum(MealType),nullable=False)
    quantity = Column(Integer,default=0)
    settled = Column(Boolean,default=False)


class Dine_in(Base):
    __tablename__ = "dine_in"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    subscription_id = Column(UUID(as_uuid=True),ForeignKey("subscriptions.id"),nullable=False)
    date = Column(Date,nullable=False)
    meal_type = Column(Enum(MealType),nullable=False)
    scanned_at = Column(Time,nullable=False)
    verified = Column(Boolean,default=True)

class Delivery_logs(Base):
    __tablename__ = "logs"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    service_id = Column(UUID(as_uuid=True),ForeignKey("tiffin_services.id"),nullable=False)
    date = Column(Date,nullable=False)
    meal_type = Column(Enum(MealType),nullable =False)
    delivered = Column(Boolean,default=True)


class Menu(Base):
    __tablename__ = "menu"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    service_id = Column(UUID(as_uuid=True),ForeignKey("tiffin_services.id"),nullable=False)
    date = Column(Date,nullable=False)
    meal_type = Column(Enum(MealType),nullable=False)
    items = Column(JSON,nullable=False)


class DeliveryPartner(Base):
    __tablename__ = 'delivery_partners'
    
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    user_id = Column(String, nullable=False)
    service_id = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False)
    assigned_at = Column(DateTime, nullable=False)


class DeliveryQtyOverrides(Base):
    __tablename__ = 'delivery_qty_overrides'
    
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    user_id = Column(String, nullable=False)
    service_id = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    meal_type = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
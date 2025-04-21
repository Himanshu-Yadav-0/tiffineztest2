from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DeliveryPartner(Base):
    __tablename__ = 'delivery_partners'
    
    id = Column(String, primary_key=True)
    user_id = Column(String, nullable=False)
    service_id = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False)
    assigned_at = Column(DateTime, nullable=False)
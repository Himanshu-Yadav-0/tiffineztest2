from sqlalchemy import Column, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TempDeliveryRequest(Base):
    __tablename__ = 'temp_delivery_requests'

    id = Column(String, primary_key=True)
    user_id = Column(String, nullable=False)
    service_id = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    meal_type = Column(String, nullable=False)

    def __repr__(self):
        return f"<TempDeliveryRequest(id={self.id}, user_id={self.user_id}, service_id={self.service_id}, date={self.date}, meal_type={self.meal_type})>"
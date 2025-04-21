from sqlalchemy import Column, String, Integer, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(String, primary_key=True)  # Assuming 'id' is a string (e.g., 'SUB1', 'SUB2')
    user_id = Column(String, nullable=False)
    service_id = Column(String, nullable=False)
    total_tiffins = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    loan_allowed = Column(Boolean, nullable=False)
    default_meal_mode = Column(String, nullable=False)

    def __repr__(self):
        return f"<Subscription(id={self.id}, user_id={self.user_id}, service_id={self.service_id}, " \
               f"total_tiffins={self.total_tiffins}, start_date={self.start_date}, " \
               f"end_date={self.end_date}, loan_allowed={self.loan_allowed}, " \
               f"default_meal_mode={self.default_meal_mode})>"
from sqlalchemy import create_engine, Column, String, Date, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class
Base = declarative_base()

# Define the delivery_qty_overrides table
class DeliveryQtyOverrides(Base):
    __tablename__ = 'delivery_qty_overrides'
    
    id = Column(String, primary_key=True)
    user_id = Column(String, nullable=False)
    service_id = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    meal_type = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)

# Create an SQLite engine (change connection string as needed)
engine = create_engine('sqlite:///database.db')

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
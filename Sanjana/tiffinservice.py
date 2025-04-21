from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a base class
Base = declarative_base()

# Define the TiffinService model
class TiffinService(Base):
    __tablename__ = 'tiffin_services'

    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    location = Column(String)
    owner_id = Column(String)

    def __repr__(self):
        return f"<TiffinService(id='{self.id}', name='{self.name}', location='{self.location}')>"

# Database connection
engine = create_engine('sqlite:///tiffin_services.db')  # Example using SQLite
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()
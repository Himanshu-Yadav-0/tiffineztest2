from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Define base class
Base = declarative_base()

# Define the TiffinService model
class TiffinService(Base):
    __tablename__ = 'tiffin_services'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    location = Column(String, nullable=False)
    owner_id = Column(String, nullable=False)

# Set up database engine and session (no data inserted)
engine = create_engine('sqlite:///tiffin_services.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

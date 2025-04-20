from app.db.database import Base
from sqlalchemy import Column, String, Integer

class TestModel(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

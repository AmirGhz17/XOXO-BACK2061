from sqlalchemy import Column, Integer, String
from database import Base
class User(Base):
    __tablename__ = "users"

    name = Column(String, primary_key=True)
    score = Column(Integer)

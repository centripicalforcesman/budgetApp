from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Budget(Base):
    __tablename__ = "budget"

    id = Column(Integer, primary_key=True)
from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata

class Budget(Base):
    __tablename__ = "budgets.budget"

    id: Mapped[int] =  mapped_column(primary_key=True)
    month: Mapped[int] = mapped_column(nullable=False)#will eventually be enum for month
    year: Mapped[int] = mapped_column(nullable=False)


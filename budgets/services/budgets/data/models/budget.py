from __future__ import annotations
from typing import List
from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata

class Budget(Base):
    __tablename__ = "budget"

    id: Mapped[int] =  mapped_column(primary_key=True)
    month: Mapped[int] = mapped_column(nullable=False)#will eventually be enum for month
    year: Mapped[int] = mapped_column(nullable=False)
    budgetGroups: Mapped[List["BudgetGroup"]] = relationship(back_populates="budget")


from __future__ import annotations
from typing import List
from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from budgets.services.budgets.data.database import Base  # Import shared Base
#from budgets.services.budgets.data.models.budget import BudgetGroup
#test comment

class Budget(Base):
    __tablename__ = "budget"

    id: Mapped[int] =  mapped_column(primary_key=True)
    month: Mapped[int] = mapped_column(nullable=False)#will eventually be enum for month
    year: Mapped[int] = mapped_column(nullable=False)
    budgetGroups: Mapped[List["BudgetGroup"]] = relationship("BudgetGroup", back_populates="budget")


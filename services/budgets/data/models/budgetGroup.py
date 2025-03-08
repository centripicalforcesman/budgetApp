from __future__ import annotations
from typing import List
from sqlalchemy import Column, DateTime, Integer, func, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from services.budgets.data.database import Base

class BudgetGroup(Base):
    __tablename__ = "budgetGroup"

    id: Mapped[int] =  mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    budgetId: Mapped[int] = mapped_column(Integer, ForeignKey("budget.id"))
    budget: Mapped["Budget"] = relationship("Budget", back_populates="budgetGroups")


from __future__ import annotations
from typing import List
from decimal import Decimal
from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from services.budgets.data.database import Base

class BudgetItem(Base):
    __tablename__ = "budgetItem"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    allocatedAmount: Mapped[Decimal] = mapped_column(default=0.00)
    saving: Mapped[bool] = mapped_column(default=False)


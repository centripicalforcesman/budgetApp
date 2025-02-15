from sqlalchemy import Column, DateTime, Integer, func, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


Base = declarative_base()
metadata = Base.metadata

class BudgetGroup(Base):
    __tablename__ = "budgets.budgetGroup"

    id: Mapped[int] =  mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)


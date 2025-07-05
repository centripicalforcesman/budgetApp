from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from services.budgets.data.repos.budgetRepo import budgetRepo
from services.budgets.data.database import Base

#TODO: move to data layer
engine  = create_engine(
    "postgresql://postgres:password@localhost/budget_db",
    echo=True)

Base.metadata.create_all(engine)
class GetBudgetByYearMonth: 
    def Execute(self, year, month):
        with Session(engine) as session:
            repo = budgetRepo(session, [])
            return repo.get_by_year_month(year, month).serialize()

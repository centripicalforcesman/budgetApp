from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from services.budgets.data.repos.budgetRepo import budgetRepo
from services.budgets.data.database import Base


engine  = create_engine(
    "postgresql://postgres:password@localhost/budget_db",
    echo=True)

Base.metadata.create_all(engine)
class GetBudget: 
    def Execute(self, id):
        with Session(engine) as session:
            repo = budgetRepo(session, [])
            budget = repo.get_by_id(id)
            return repr(budget)

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from budgets.services.budgets.data.repos.budgetRepo import budgetRepo
from budgets.services.budgets.data.database import Base


engine  = create_engine(
    "postgresql://postgres:password@localhost/budget_db",
    echo=True)

Base.metadata.create_all(engine)
class GetBudget: 
    def Execute(self, id):
        with Session(engine) as session:
            try: 
                repo = budgetRepo(session, [])
                budget = repo.get_by_id(id)
                return repr(budget)
            except Exception as e:
                return str(e) #handle these errors better before prod

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from services.budgets.data.models.budget import Budget
from services.budgets.mappers.budgetMappers import budget_data_to_budget_domain
from services.budgets.data.database import Base

engine  = create_engine(
    "postgresql://postgres:password@localhost/budget_db",
    echo=True)

Base.metadata.create_all(engine)

class budgetRepo:
    def __init__(self, identity_map=None):
        self.__identity_map = identity_map or dict()
    
    def get_by_id(self,id):
        with Session(engine) as session:
            budget = session.query(Budget).get(id)
            return budget_data_to_budget_domain(budget)
    
    def get_by_year_month(self, year, month):
        with Session(engine)as session:
            budget = session.query(Budget).filter(Budget.year == year, Budget.month == month).one()
            return budget_data_to_budget_domain(budget)
    
        


from sqlalchemy.orm import Session
from services.budgets.data.models.budget import Budget
from services.budgets.mappers.budgetMappers import budget_data_to_budget_domain

class budgetRepo:
    def __init__(self, session: Session, identity_map=None):
        self.session = session
        self.__identity_map = identity_map or dict()
    
    def get_by_id(self,id):
        budget = self.session.query(Budget).get(id)
        return budget_data_to_budget_domain(budget)
        


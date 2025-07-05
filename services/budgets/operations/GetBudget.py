from services.budgets.data.repos.budgetRepo import budgetRepo

class GetBudget: 
    def Execute(self, id):
        repo = budgetRepo([])
        return repo.get_by_id(id).serialize()

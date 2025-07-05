from services.budgets.data.repos.budgetRepo import budgetRepo

class GetBudgetByYearMonth: 
    def Execute(self, year, month):
        repo = budgetRepo([])
        return repo.get_by_year_month(year, month).serialize()

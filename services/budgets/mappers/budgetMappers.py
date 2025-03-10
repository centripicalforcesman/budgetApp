from services.budgets.data.models import budget as budgetDataModel
from services.budgets.domain.models.budget import Budget
from services.budgets.mappers.budgetGroupMappers import budgetGroups_data_to_budgetGroups_domain

def budget_data_to_budget_domain(instance: budgetDataModel) -> Budget:
    return Budget(instance.id, 
                  instance.month, 
                  instance.year,
                  budgetGroups_data_to_budgetGroups_domain(instance.budgetGroups))

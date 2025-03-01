from budgets.services.budgets.data.models import budget as budgetDataModel
from budgets.services.budgets.domain.models.budgetGroup import Budget

def budget_data_to_budget_domain(instance: budgetDataModel) -> Budget:
    return Budget(instance.id, instance.month, year = instance.year)

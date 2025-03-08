from typing import List
from services.budgets.data.models.budgetGroup import BudgetGroup as budgetGroupDataModel
from services.budgets.domain.models.budgetGroup import BudgetGroup

def budgetGroup_data_to_budgetGroup_domain(instance: budgetGroupDataModel) -> BudgetGroup:
    return BudgetGroup(instance.id, instance.name)

def budgetGroups_data_to_budgetGroups_domain(instances: List[budgetGroupDataModel]) -> List[BudgetGroup]:
    return [budgetGroup_data_to_budgetGroup_domain(instance) for instance in instances]

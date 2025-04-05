from typing import List
from services.budgets.data.models.budgetItem import BudgetItem as budgetItemDataModel
from services.budgets.domain.models.budgetItem import BudgetItem

def budgetItem_data_to_budgetItem_domain(instance: budgetItemDataModel) -> BudgetItem:
    return BudgetItem(instance.id, instance.name, instance.allocatedAmount, instance.saving)

def budgetItems_data_to_budgetItems_domain(instances: List[budgetItemDataModel]) -> List[BudgetItem]:
    return [budgetItem_data_to_budgetItem_domain(instance) for instance in instances]

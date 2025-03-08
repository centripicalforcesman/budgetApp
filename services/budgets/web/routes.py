from flask import Blueprint
from services.budgets.operations.GetBudget import GetBudget

budgetsBp = Blueprint('budgets', __name__)

@budgetsBp.route('/budgets/<int:budgetID>')
def budgets(budgetID):
   getBudget = GetBudget()
   return getBudget.Execute(budgetID)
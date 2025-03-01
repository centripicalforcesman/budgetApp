from flask import Blueprint
from budgets.services.budgets.GetBudget import GetBudget

bp = Blueprint('budgets', __name__)

@bp.route('/budgets/<int:budgetID>')
def budgets(budgetID):
   getBudget = GetBudget()
   return getBudget.Execute(budgetID)
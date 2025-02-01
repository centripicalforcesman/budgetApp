from flask import Blueprint
from .services.GetBudget import GetBudget

bp = Blueprint('budgets', __name__)

@bp.route('/budgets/<int:budgetID>')
def budgets(budgetID):
   getBudget = GetBudget()
   return getBudget.Execute(budgetID)
from flask import Blueprint, jsonify
from services.budgets.operations.GetBudget import GetBudget


budgetsBp = Blueprint('budgets', __name__)

@budgetsBp.route('/budgets/<int:budgetID>')
def budgets(budgetID):
   getBudget = GetBudget()
   budget = getBudget.Execute(budgetID)
   return jsonify(budget)
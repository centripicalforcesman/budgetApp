from flask import Blueprint, jsonify
from services.budgets.operations.GetBudget import GetBudget
from services.budgets.operations.GetBudgetByYearMonth import GetBudgetByYearMonth


budgetsBp = Blueprint('budgets', __name__)

@budgetsBp.route('/budgets/<int:budgetID>')
def budgets(budgetID):
   getBudget = GetBudget()
   budget = getBudget.Execute(budgetID)
   return jsonify(budget)

@budgetsBp.route('/budgets/<int:year>/<int:month>')
def budgetsByYearMonth(year, month):
   getBudget = GetBudgetByYearMonth()
   budget = getBudget.Execute(year, month)
   return jsonify(budget)
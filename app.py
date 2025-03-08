from flask import Flask
from services.budgets.web.routes import budgetsBp
app = Flask(__name__)

app.register_blueprint(budgetsBp)

@app.route("/")
def home():
    return "Hello, Flask budget app"
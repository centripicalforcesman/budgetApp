from flask import Flask
from flask_cors import CORS
from services.budgets.web.routes import budgetsBp


app = Flask(__name__)


app.register_blueprint(budgetsBp)

CORS(app)

@app.route("/")
def home():
    return "Hello, Flask budget app"
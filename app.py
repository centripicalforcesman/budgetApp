from flask import Flask
from budgets.routes import bp
app = Flask(__name__)

app.register_blueprint(bp)

@app.route("/")
def home():
    return "Hello, Flask budget app"
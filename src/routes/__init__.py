from flask import Flask
from flask_login import LoginManager

app = Flask(__name__, template_folder='templates')
app.secret_key = "super secret key"
login_manager = LoginManager(app)


from flask import Flask,g
from flask_login import LoginManager


app = Flask(__name__, template_folder='templates')
login_manager = LoginManager(app)






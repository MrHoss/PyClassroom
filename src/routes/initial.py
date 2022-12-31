from flask import render_template
from flask_login import login_required
from sqlalchemy import join

from src.database.connect import session
from src.database.models import Users,Roles,roles_users


def initialRoutes(app):

    @app.route('/',methods=['GET'])
    @login_required
    def home():
        return render_template('pages/home.jinja',title="Home")

    @app.route('/settings/',methods=['GET'])
    @login_required
    def settings():
        return render_template('pages/settings.jinja',title='Configurações')


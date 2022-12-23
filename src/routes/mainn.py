from functools import wraps
from flask import Flask,render_template,request,abort,redirect
from flask_login import login_required,login_manager
from src.services.interfaceController import InterfaceController
from src.database.connect import session



def mainRoutes(app):
    
    @app.route('/',methods=['GET'])
    @login_required
    def home():
        return render_template('pages/home.jinja',title="Home")

    @app.route('/settings/',methods=['GET'])
    @login_required
    def settings():
        return render_template('pages/settings.jinja',title='Configurações')


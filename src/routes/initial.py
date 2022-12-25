from flask import render_template
from flask_login import login_required

def initialRoutes(app):
    
    @app.route('/',methods=['GET'])
    @login_required
    def home():
        return render_template('pages/home.jinja',title="Home")

    @app.route('/settings/',methods=['GET'])
    @login_required
    def settings():
        return render_template('pages/settings.jinja',title='Configurações')


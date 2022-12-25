from flask import render_template
from flask_login import login_required

def secretaryRoutes(app):
    @app.route('/secretary/',methods=['GET'])
    @login_required
    def secretary():
        return render_template('pages/secretary.jinja',title="Secretaria Digital")



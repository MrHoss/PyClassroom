from flask import render_template
from flask_login import login_required

def libraryRoutes(app):
    @app.route('/library/',methods=['GET'])
    @login_required
    def library():
        return render_template('pages/library.jinja',title="Biblioteca")



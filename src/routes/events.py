from flask import render_template
from flask_login import login_required

def eventsRoutes(app):
    @app.route('/events/',methods=['GET'])
    @login_required
    def events():
        return render_template('pages/events.jinja',title="Eventos")



from src.routes import auth,quizzpp,_errors_,setup,initial,secretary,library,events,studying,admin,materials
from src.routes import app
from src.database.models import Users,Roles,roles_users
from src.database.connect import session
from flask import g


def get_user():
    if 'user' not in g:
        with session:
            g.user = session.query(Users).join(roles_users).join(Roles).filter(Users.email == 'admin@example.com').first()
        session.close()
    return g.user

@app.context_processor
def inject_user():
    return {'user': get_user()}

def Routes():
    
    auth.authenticationRoutes(app)
    studying.studyingRoutes(app)
    materials.materialRoutes(app)
    initial.initialRoutes(app)
    secretary.secretaryRoutes(app)
    library.libraryRoutes(app)
    events.eventsRoutes(app)
    admin.dashboardRoutes(app)
    _errors_.errorsRoutes(app)
    setup.setupRoute(app)

    quizzpp.quizzppRoute(app)
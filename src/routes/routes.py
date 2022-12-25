from src.routes import auth,quizzpp,_errors_,setup,initial,secretary,library,events
from src.routes import app

def Routes():
    
    auth.authenticationRoutes(app)
    initial.initialRoutes(app)
    secretary.secretaryRoutes(app)
    library.libraryRoutes(app)
    events.eventsRoutes(app)
    _errors_.errorsRoutes(app)
    setup.setupRoute(app)

    quizzpp.quizzppRoute(app)
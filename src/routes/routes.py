from src.routes import auth,quizzpp,mainn,_errors_,setup
from src.routes import app

def Routes():
    
    auth.authenticationRoutes(app)
    mainn.mainRoutes(app)
    _errors_.errorsRoutes(app)
    setup.setupRoute(app)

    quizzpp.quizzppRoute(app)
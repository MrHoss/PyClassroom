from flask import Flask,render_template,request,redirect
from src.database.connect import session
    
def errorsRoutes(app):
    @app.errorhandler(404)
    def page_not_found(error):
        session.rollback()
        session.close_all()
        print(error)
        return render_template('pages/404.jinja', title = '404'), 404

    @app.errorhandler(401)
    def unauthorized_access(error):
        session.rollback()
        session.close_all()
        print(error)
        return redirect('/login')

    @app.errorhandler(500)
    def internal_server_error(error):
        session.rollback()
        session.close_all()
        print(error,'salve')
        return f"Erro {error.code}: {error.description}", 500
from flask import Flask,render_template,request,redirect
    
def errorsRoutes(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('pages/404.jinja', title = '404'), 404

    @app.errorhandler(401)
    def unauthorized_access(error):
        return redirect('/login')
from flask import Flask,render_template,request

def quizzppRoute(app):
    @app.route('/quizzpp/',methods=['GET'])
    def quizzpp():
        return render_template('/games/quizzpp/index.jinja',title="Quizz++")

    @app.route('/quizzpp/<string:urlRoute>/')
    def quizzppPages(urlRoute):
            return render_template('/games/quizzpp/{}.jinja'.format(urlRoute.lower()),title=urlRoute)
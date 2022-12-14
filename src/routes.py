from flask import Flask,render_template,request

app = Flask(__name__, template_folder='templates')

#EDUCA++ ROUTES
@app.route('/',methods=['GET'])
def home():
    return render_template('pages/home.jinja',title="Home",role="student")
@app.route('/<string:Discipline>/',methods=['GET'])
def MainPages(Discipline):
    return render_template('pages/{}.jinja'.format(Discipline.lower()),title=Discipline,role="tutor")

#END OF EDUCA++ ROUTES

#QUIZZPP ROUTES
@app.route('/quizzpp',methods=['GET'])
def quizzpp():
    return render_template('/games/quizzpp/index.jinja',title="Quizz++")

@app.route('/quizzpp/<string:Discipline>/')
def quizzppPages(Discipline):
    return render_template('/games/quizzpp/{}.jinja'.format(Discipline.lower()),title=Discipline)
#END OF QUIZZPP ROUTES


@app.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text



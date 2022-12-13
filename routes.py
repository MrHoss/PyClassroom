from flask import Flask,render_template,request

app = Flask(__name__, template_folder='templates')

#EDUCA++ ROUTES
@app.route('/',methods=['GET'])
def home():
    return render_template('/home.html',title="Home")

@app.route('/biology/',methods=['GET'])
def biology():
    return render_template('/biology.html',title="Biologia")

@app.route('/history/',methods=['GET'])
def history():
    return render_template('/history.html',title="History")

@app.route('/jogos/',methods=['GET'])
def games():
    return render_template('/educa-student/games.html',title="Jogos")
#END OF EDUCA++ ROUTES

#QUIZZPP ROUTES
@app.route('/quizzpp',methods=['GET'])
def quizzpp():
    return render_template('/games/quizzpp/index.html',title="Quizz++")

@app.route('/quizzpp/matematica/', methods=['GET'])
def quizzppMath():
    return render_template('/games/quizzpp/math.html',title="Quizz++ Matemática")

@app.route('/quizzpp/geografia/')
def quizzppGeography():
    return render_template('/games/quizzpp/geography.html',title="Quizz++ Geografia")

@app.route('/quizzpp/historia/')
def quizzppHistory():
    return render_template('/games/quizzpp/history.html',title="Quizz++ História")

@app.route('/quizzpp/quimica/')
def quizzppScience():
    return render_template('/games/quizzpp/science.html',title="Quizz++ Química")

@app.route('/quizzpp/biologia/')
def quizzppBiology():
    return render_template('/games/quizzpp/biology.html',title="Quizz++ Biologia")

@app.route('/quizzpp/fisica/')
def quizzppPhysic():
    return render_template('/games/quizzpp/physic.html',title="Quizz++ Física")

@app.route('/quizzpp/astronomia/')
def quizzppAstronomy():
    return render_template('/games/quizzpp/astronomy.html',title="Quizz++ Astronomia")

@app.route('/quizzpp/tecnologia/')
def quizzppTechnology():
    return render_template('/games/quizzpp/technology.html',title="Quizz++ Tecnologia")
#END OF QUIZZPP ROUTES


@app.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text



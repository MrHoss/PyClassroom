from flask import Flask,render_template,request
#from src.services.interfaceController import InterfaceController


app = Flask(__name__, template_folder='templates')       
Role = "tutor"
    
#EDUCA++ ROUTES
@app.route('/',methods=['GET'])
def home():
    return render_template('pages/home.jinja',title="Home",role=Role)

@app.route('/<urlRoute>/',methods=['GET'])
def MainPages(urlRoute):
    #Interface = InterfaceController.controllerMainPgs(urlRoute)
    return render_template('pages/{}.jinja'.format(urlRoute),interface='Interface',title=urlRoute,role=Role)



#END OF EDUCA++ ROUTES

#QUIZZPP ROUTES
@app.route('/quizzpp',methods=['GET'])
def quizzpp():
    return render_template('/games/quizzpp/index.jinja',title="Quizz++")

@app.route('/quizzpp/<string:urlRoute>/')
def quizzppPages(urlRoute):
        return render_template('/games/quizzpp/{}.jinja'.format(urlRoute.lower()),title=urlRoute)
    
#END OF QUIZZPP ROUTES

"""@app.errorhandler(404)
def page_not_found(error):
   return errorPage404()"""
   

@app.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text



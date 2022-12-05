from flask import Flask,render_template

app = Flask(__name__, template_folder='pages')
@app.route('/')
def hello():
    return render_template('/index.html')


@app.route('/matematica/')
def about():
    return render_template('/matematica.html')
    
@app.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text

if __name__ == "__main__":
    app.run(debug=True)

from functools import wraps
from flask import render_template,request, redirect
from flask_login import login_user, logout_user
from src.database.models import Users
from src.database.connect import session



def authenticationRoutes(app):
    @app.route('/login/',methods=['GET','POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            pwd = request.form['password']

            user = Users.query.filter_by(email=email).first()

            if not user or not user.verify_password(pwd):
                return redirect('/login')
            else:
                login_user(user)
                return redirect('/')
        return render_template('pages/login.jinja',title="Home")
        
    @app.route('/register',methods=['GET','POST'])
    def register():
        if request.method == 'POST':
            name = request.form['username']
            email = request.form['email']
            pwd = request.form['password']

            user = Users(name, email,pwd)
            session.add(user)
            session.commit()
            return redirect('/') 
            
        return render_template('pages/register.jinja',title="Home")

    @app.route('/logout',methods=['GET','POST'])
    def logout():
        logout_user()
        return redirect('/login')
import datetime
from functools import wraps
from flask import render_template,request, redirect,abort
from flask_login import login_user, logout_user,login_required
from src.database.models import Users,Roles
from src.database.connect import session
from sqlalchemy.exc import IntegrityError

def authenticationRoutes(app):
    @app.route('/login/',methods=['GET','POST'])
    @app.route('/login',methods=['GET','POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            pwd = request.form['password']

            user = Users.query.filter_by(email=email).first()
            if not user or not user.verifyPassword(pwd):
                return redirect('/login')
            else:
                login_user(user)
                session.close()
                return redirect('/')
        return render_template('pages/login.jinja',title="Login ")
        
    @app.route('/register/',methods=['GET','POST'])
    def register():
        if request.method == 'POST':
            name = request.form['username']
            email = request.form['email']
            pwd = request.form['password']
            with session:
                role = session.query(Roles).filter(Roles.name == 'Estudante').first()
                user = Users(name, email, pwd, updatedAt=datetime.datetime.utcnow(), createdAt=datetime.datetime.utcnow(), roles=[role])
            try:
                session.add(user)
                session.commit()
                return redirect('/') 
            except IntegrityError as e:
                print(e)
                abort(409,'this_user_already_exists')
            finally:
                session.rollback()
                session.close()
        return render_template('pages/register.jinja',title="Home")

    @app.route('/logout/',methods=['GET'])
    @login_required
    def logout():
        logout_user()
        session.close()
        return redirect('/login')
import datetime
from flask import render_template,request,redirect,abort
from flask_security import login_required,roles_accepted
from src.database.connect import session
from src.database.models import Roles,Users
from sqlalchemy.exc import IntegrityError

def dashboardRoutes(app):
    @app.route('/dashboard',methods=['GET','POST'])
    @login_required
    @roles_accepted('Admin')
    def dashboard():
        if request.method == 'POST':
            name = request.form['username']
            email = request.form['email']
            pwd = request.form['password']
            with session:
                role = session.query(Roles).filter(Roles.name == 'Professor').first()
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
        return render_template('pages/dashboard.jinja',title="Dashboard")



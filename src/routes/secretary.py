from flask import render_template
from flask_login import login_required
from src.database.models import Users,Roles,roles_users
from src.database.connect import session
from sqlalchemy.orm import joinedload

def secretaryRoutes(app):
    @app.route('/secretary/',methods=['GET'])
    @login_required
    def secretary():
        return render_template('pages/secretary.jinja',title="Secretaria Digital")

    @app.route('/secretary/students',methods=['GET'])
    @login_required
    def secretary_students():
        with session:
            query = (
                session.query(Roles, Users)
                .join(roles_users, Roles.id == roles_users.c.role_id)
                .join(Users, Users.id == roles_users.c.user_id)
            )
            query = query.filter(Roles.name == "Estudante")
            query = query.options(joinedload(Users.roles))
            admin_users = query.all()
        session.close()
        return render_template('pages/secretary/students.jinja',title="Secretaria Digital", students = admin_users)



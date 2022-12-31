import json
from flask import render_template,abort
from flask_security import login_required, roles_accepted
from src.database.models import Disciplines,Materials
from src.database.connect import session
from sqlalchemy import func

def studyingRoutes(app):
    @app.route('/studying/',methods=['GET'])
    @login_required
    @roles_accepted('Estudante')
    def studying():
        with session:
            disciplines = session.query(Disciplines).all()
        return render_template('pages/studying.jinja',title="Estudar", disciplines=disciplines)


    @app.route('/studying/<discipline_tagname>/',methods=['GET'])
    @login_required
    @roles_accepted('Estudante')
    def classes(discipline_tagname):
        with session:
            classes = (
                session.query(Materials,Disciplines)
                .join(Disciplines, Materials.disciplines)
                .filter(func.lower(Disciplines.tagName) == discipline_tagname)
                .all()
            )
        session.close()
        try:
            return render_template('pages/studying/classes.jinja',title=classes[0][1].name, classes=classes)
        except Exception as e:
            return render_template('pages/studying/classes.jinja',title='Nenhuma aula disponível', error=e)
    
    @app.route('/studying/<discipline_tagname>/<class_id>',methods=['GET'])
    @login_required
    @roles_accepted('Estudante')
    def classe(discipline_tagname,class_id):
        with session:
            classe = session.query(Materials).filter(Materials.id == class_id).first()
        session.close()
        return render_template('pages/studying/singleclass.jinja',title=classe.name, classe=classe)



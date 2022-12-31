import datetime
from flask import render_template,request,redirect,abort
from flask_login import login_required,current_user
from src.database.connect import session
from src.database.models import Disciplines,Materials,disciplines_material
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
import os

def materialRoutes(app):
    @app.route('/materials/',methods=['GET'])
    @login_required
    def materials():
        with session:
            materials = (
                session.query(Materials, Disciplines)
                .join(Disciplines, Materials.disciplines)
                .filter(Materials.author_id == current_user.id)
                .all()
            )
        session.close()
        return render_template('pages/materials.jinja',title="Materiais", Materials= materials)

    @app.route('/materials/<material_id>',methods=['GET'])
    @login_required
    def material(material_id):
        with session:
            material = (
                session.query(Materials, Disciplines)
                .join(Disciplines, Materials.disciplines)
                .filter(Materials.id == material_id)
                .first()
            )
        session.close()
        return render_template('pages/material/material-item.jinja',title=material[0].name, Material= material)

    @app.route('/add-material/',methods=['GET','POST'])
    @login_required
    def add_material():
        if request.method == 'POST':
            video_dir = 'src/medias/videos'
            if not os.path.exists(video_dir):
                os.makedirs(video_dir)
            title = request.form['title']
            description = request.form['description']
            content = request.form['content']
            discipline = request.form['disciplines']
            video = request.files["video"]
            with session:
                Discipline = session.query(Disciplines).filter(Disciplines.id == discipline).first()
                Material = Materials(title, description, content, author_id=current_user.id, updatedAt=datetime.datetime.utcnow(), createdAt=datetime.datetime.utcnow(), disciplines=[Discipline])
            try:
                video.save(os.path.join(video_dir, video.filename))
                session.add(Material)
                session.commit()
                return redirect('/add-material') 
            except Exception as e:
                abort(500,e)
            finally:
                session.rollback()
                session.close()

        if request.method == 'GET':
            with session:
                disciplines = session.query(Disciplines).all()
            session.close()

        return render_template('pages/material/add-material.jinja',title="Adicionar Material", disciplines=disciplines)



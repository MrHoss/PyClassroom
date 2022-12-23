from flask import Flask,render_template,request
from src.database.install import migrateAll,seedAll

def setupRoute(app):
    @app.route('/setup',methods=['GET'])
    def setup():

        migrateAll()
        seedAll()
        return 'Instalação concluída'
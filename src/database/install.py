#Execute this code to create all tables in database

import datetime
from src.database.models import Base,Users,Roles,Disciplines,Materials
from src.database.connect import engine,session

def migrateAll():
    Base.metadata.create_all(engine)


def seedAll():
    try:
        new_role = Roles(name='Admin', description='Administrator')
        new_user = Users(name='Admin', email='admin@example.com', password='admin', updatedAt=datetime.datetime.utcnow(), createdAt=datetime.datetime.utcnow(),roles=[new_role])
        roles = [Roles(name='Professor', description='Teacher'),Roles(name='Estudante', description='Student')]
        session.bulk_save_objects(roles)
        session.add(new_user)
        session.commit()
        session.close
    except Exception:
        print(Exception)
    try:
        disciplines = [Disciplines(name='Geografia', tagName='geography'),Disciplines(name='Matemática', tagName='math'),Disciplines(name='História', tagName='history'),]
        session.bulk_save_objects(disciplines)
        session.commit()
        session.close
    except Exception:
        print(Exception)
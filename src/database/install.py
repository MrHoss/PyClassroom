#Execute this code to create all tables in database

from src.database.models import Base,Users
from src.database.connect import engine,session

def migrateAll():
    Base.metadata.create_all(engine)


def seedAll():
    user = Users(name='Daniel', email='danielsouzaT99@hotmail.com',password='271208',role='admin')
    session.add(user)
    session.commit()
migrateAll()

from models import Users
from connect import session


user = Users(name='John', password=30)
session.add(user)
session.commit()
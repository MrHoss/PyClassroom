# users model

from sqlalchemy import Column, Integer, String,ForeignKey,DateTime,func
from src.routes import login_manager
from src.database.connect import db_session
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

Base = declarative_base()
Base.query = db_session.query_property()


@login_manager.user_loader
def get_user(user_id):
    return Users.query.filter_by(id=user_id).first()

class Users(Base, UserMixin):
    __tablename__ = 'Users'
    id = Column(Integer, autoincrement=True,primary_key=True)
    name = Column(String(150),nullable=False)
    email = Column(String(150),nullable=False)
    password = Column(String(150),nullable=False)
    role = Column(String(length=15),nullable=True)
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self,pwd):
        return check_password_hash(self.password,pwd)

    
class Disciplines(Base):
    __tablename__ = 'Disciplines'
    id = Column(Integer, autoincrement=True,primary_key=True)
    name = Column(String(150),nullable=False)
    tagName = Column(String(150),nullable=False)
    def __init__(self,name,tagName):
        self.name = name
        self.tagName = tagName
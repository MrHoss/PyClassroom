# users model

from sqlalchemy import Column, Integer, String,ForeignKey,DateTime,UniqueConstraint,func,Table
from src.routes import login_manager
from src.database.connect import session,db_session
from sqlalchemy.orm import relationship,backref
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from flask_security import RoleMixin,SQLAlchemyUserDatastore

Base = declarative_base()
Base.query = db_session.query_property()


@login_manager.user_loader
def get_user(user_id):
    with session:
        user =Users.query.filter_by(id=user_id).first()
    session.close()
    return user


roles_users = Table('roles_users', Base.metadata,Column('user_id', Integer(), ForeignKey('Users.id'),unique=True), Column('role_id', Integer(), ForeignKey('Roles.id')))

class Roles(Base, RoleMixin):
    __tablename__ = 'Roles'
    id = Column(Integer(), primary_key=True)  # pylint: disable=invalid-name
    name = Column(String(80), unique=True)
    description = Column(String(255))

class Users(Base, UserMixin):
    __tablename__ = 'Users'
    id = Column(Integer, unique=True,autoincrement=True,primary_key=True)
    name = Column(String(150),nullable=False)
    email = Column(String(150),unique=True,nullable=False)
    password = Column(String(150),nullable=False)
    roles = relationship('Roles', secondary=roles_users, backref=backref('Users', lazy='dynamic'))
    createdAt = Column(DateTime,nullable=False)
    updatedAt = Column(DateTime,nullable=False)
    UniqueConstraint('id','email',name='idx_id_email')
    def __init__(self,name,email,password,createdAt,updatedAt,roles):
        self.name = name
        self.email = email
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.roles = roles
        self.password = generate_password_hash(password)

    def verifyPassword(self,pwd):
        print(self.password)
        return check_password_hash(self.password, pwd)

user_datastore = SQLAlchemyUserDatastore(Base, Users, Roles)

disciplines_material = Table('disciplines_material', Base.metadata,Column('material_id', Integer(), ForeignKey('Materials.id'),unique=True), Column('discipline_id', Integer(), ForeignKey('Disciplines.id')))
class Disciplines(Base):
    __tablename__ = 'Disciplines'
    id = Column(Integer, autoincrement=True,primary_key=True)
    name = Column(String(150),nullable=False)
    tagName = Column(String(150),nullable=False)
    def __init__(self,name,tagName):
        self.name = name
        self.tagName = tagName

class Materials(Base):
    __tablename__ = 'Materials'
    id = Column(Integer, autoincrement=True,primary_key=True)
    name = Column(String(150),nullable=False)
    description = Column(String(255),nullable=False)
    content = Column(String(6000),nullable=False)
    author_id = Column(Integer, ForeignKey('Users.id'))
    createdAt = Column(DateTime,nullable=False)
    updatedAt = Column(DateTime,nullable=False)
    disciplines = relationship('Disciplines', secondary=disciplines_material, backref=backref('Materials', lazy='dynamic'))
    author = relationship("Users", backref=backref("Materials", cascade="all, delete-orphan"))

    def __init__(self,name,description,content,disciplines,author_id,updatedAt,createdAt):
        self.name = name
        self.description = description
        self.content = content
        self.disciplines = disciplines
        self.author_id = author_id
        self.updatedAt = updatedAt
        self.createdAt = createdAt
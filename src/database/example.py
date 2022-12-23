from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a connection to the database
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/educa-db')

# Declare a base for the models
Base = declarative_base()

# Define a model class
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to execute queries
Session = sessionmaker(bind=engine)
session = Session()

# Add a user to the database
user = User(name='John', age=30)
session.add(user)
session.commit()

# Query the database
users = session.query(User).all()
for user in users:
    print(user.name, user.age)
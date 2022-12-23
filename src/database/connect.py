#Connect to your database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session, sessionmaker


# Create database engine
#engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/educa-db')
engine = create_engine('sqlite:///educa-db.sqlite3')

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

# Create database session
Session = sessionmaker(bind=engine)
session = Session()

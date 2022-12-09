from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# Create a database engine
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

engine = create_engine('sqlite:///database.db',connect_args={"check_same_thread":False})


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
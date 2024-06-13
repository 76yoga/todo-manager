from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an SQLite database engine
SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a sessionmaker object for interacting with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

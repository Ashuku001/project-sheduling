from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()

DB_URL = f"postgresql://ashukuezra:admin@localhost:5432/postgres"

engine = create_engine(DB_URL)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()
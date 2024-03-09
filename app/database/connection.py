# qanundaan-backend/app/database/connection.py

from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings

DATABASE_URL = settings.DATABASE_URL

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal: sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()

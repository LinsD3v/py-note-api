from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Sesionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

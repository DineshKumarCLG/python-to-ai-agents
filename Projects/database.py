from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLACLHEMY_DATABASE_URL="sqlite:///./expenses.db"

engine=create_engine(SQLACLHEMY_DATABASE_URL,connect_args={"check_same_thread":False})

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()
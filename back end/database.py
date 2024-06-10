from sqlalchemy import URL, Column, Integer, MetaData, String, Table, create_engine, select 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
url = URL.create(
    drivername="postgresql",
    username="postgres",
    host="localhost",
    database="xo",
    password="admin",
    port= 5432
)


engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


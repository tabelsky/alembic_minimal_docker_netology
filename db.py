from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

from config import PG_HOST, PG_PORT, PG_USER, PG_PASSWORD, PG_DB

engine = create_engine(f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}')


Base = declarative_base(bind=engine)


class Entity(Base):

    __tablename__ = 'some_entity'

    id = Column(Integer, primary_key=True)
    field = Column(String)

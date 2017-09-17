from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('', echo=True)
Base = declarative_base()


class GenericClass(Base):
    pass

    def __repr__(self):
        _str = "<GenericClass >"
        return _str.format()


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

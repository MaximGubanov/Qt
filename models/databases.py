from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DATETIME, BIGINT

DATABASE_NAME = 'application.sqlite'

engine = create_engine(f'sqlite:///{DATABASE_NAME}', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    loggin = Column(String)
    password = Column(String)

    def __init__(self, name, lastname, password):
        self.name = name
        self.lastname = lastname
        self.loggin = name
        self.password = password

    def __repr__(self):
        return f'User: {self.name}, {self.fullname}, {self.password}'


class HistoryClient(Base):
    __tablename__ = 'History'

    id = Column(Integer, primary_key=True)
    time_loggin = Column(DATETIME)
    ip_address = Column(BIGINT)


class ContactList(Base):
    __tablename__ = 'Contacts'

    id = Column(Integer, primary_key=True)
    id_owner = Column(Integer)
    id_client = Column(Integer)


def create_db():
    Base.metadata.create_all(engine)
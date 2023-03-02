from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

USUARIO = 'marcelo'
SENHA = 'marcelo123'
HOST = 'localhost'
BANCO = 'syslogin'
PORT = '3306'

CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Cadastro(Base):
    __tablename__ = 'Pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(200))
    senha = Column(String(100))


Base.metadata.create_all(engine)

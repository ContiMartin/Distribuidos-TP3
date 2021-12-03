from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime

class User(declarative_base()):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    edad = Column(Integer)
    sexo = Column(String)
    password = Column(String)
    fecha = Column(String)
 
    def __init__(self, name, edad, sexo, username, password, fecha):
        self.name = name
        self.edad = edad
        self.sexo = sexo
        self.username = username
        self.password = password
        self.fecha = fecha
#!/usr/bin/python3
import os
import cgi
import cgitb
import json
import sqlalchemy
import logging
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

cgitb.enable()

logger = logging.getLogger()

print("Content-Type: application/json;charset=utf-8")
print()

db_string = "postgresql://admin:admin@tl3_db:5432/tl3"
engine = create_engine(db_string, echo=False)

metadata = MetaData()

users_table = Table('users', metadata,
     Column('id', Integer, primary_key=True),
     Column('username', String),
     Column('name', String),
     Column('sexo', String),
     Column('edad', Integer),
     Column('password', String),
     Column('fehca', String),
)


metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()


class User(declarative_base()):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)    
    name = Column(String)
    sexo = Column(String)
    edad = Column(Integer)
    password = Column(String)
    fecha = Column(String)

    def __init__(self, username, name, sexo, edad, password, fecha):
        self.username = username
        self.name = name
        self.sexo = sexo
        self.edad = edad
        self.password = password
        self.fecha = fecha

def query_users():
    users = []
    for u in session.query(User).all():
        user = u.__dict__
        user.pop('_sa_instance_state', None)    
        users.append(user)
    return users

def update_user():
    try:
        form = cgi.FieldStorage()
        #user = query_users()
        user = User(
            form.getvalue('id'),
            form.getvalue('username'),
            form.getvalue('name'),
            form.getvalue('sexo'),
            form.getvalue('edad'),
            form.getvalue('password'),
            form.getvalue('fecha')
            )
        session.update(user)
        session.commit()
        return {'error': False}
    except:
        return {'error': True}

def create_user():
    try:
        form = cgi.FieldStorage()
        user = User(
            form.getvalue('username'),
            form.getvalue('name'),
            form.getvalue('sexo'),
            form.getvalue('edad'),
            form.getvalue('password'),
            form.getvalue('fecha')
            )
        session.add(user)
        session.commit()
        return {'error': False}
    except:
        return {'error': True}    

if os.environ['REQUEST_METHOD'] == 'GET':
    response = query_users()    
if os.environ['REQUEST_METHOD'] == 'POST':
    response = create_user()
if os.environ['REQUEST_METHOD'] == 'PUT':
    response = update_user()
if not response:
    response = {}

print(json.JSONEncoder().encode(response))
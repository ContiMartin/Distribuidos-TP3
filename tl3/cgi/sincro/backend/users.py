#!/usr/bin/python3
import os
import cgi
import cgitb
import json
import logging
from datetime import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from model import User

cgitb.enable()

logger = logging.getLogger()

db_string = "postgresql://admin:admin@tl3_db:5432/tl3"
engine = create_engine(db_string, echo=False)

metadata = MetaData()

metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()

def query_users():
    users = []
    for u in session.query(User).all():
        user = {
            "id": u.id,
            "name": u.name,
            "edad": u.edad,
            "sexo": u.sexo,
            "username": u.username,
            "password": u.password,
            "fecha": u.fecha
            }
        users.append(user)
    return users


def create_user():
    try:
        form = cgi.FieldStorage()
        user = User(
            form.getvalue('name'),
            form.getvalue('edad'),
            form.getvalue('username'),
            form.getvalue('sexo'),
            form.getvalue('password'),
            form.getvalue('fecha')
        )
        session.add(user)
        session.commit()
        return {'error': False}
    except Exception as e:
        logger.error(f"Error: {e}")
        return {'error': True}

def render_template(users):
    print("Content-Type: text/html;charset=utf-8 \n")
    print()
    with open('/usr/local/apache2/htdocs/index.html') as f:
        for line in f.readlines():
            print(line)
            if '<tbody id="users_tbody">' in line:
                for user in users:
                    btn = f'<td><a class="btn btn-info">Modificar</a></td>'
                    print(f'<tr><th scope="row">{user.get("id")}</th>')
                    print(f'<td>{user.get("name")}</td>')
                    print(f'<td>{user.get("edad")}</td>')
                    print(f'<td>{user.get("sexo")}</td>')
                    print(f'<td>{user.get("username")}</td>')
                    print(f'<td>{user.get("password")}</td>')
                    print(f'<td>{user.get("fecha")}</td>')
                    print(f'{btn}</tr>')

def get_user(username, password):
    return session.query(User).filter(User.username == username, User.password == password).first()
    
if os.environ['REQUEST_METHOD'] == 'GET':
    response = query_users()
if os.environ['REQUEST_METHOD'] == 'POST':
    response = create_user()
    if response:
        response = query_users()
if not response:
    response = {}
    
render_template(response)
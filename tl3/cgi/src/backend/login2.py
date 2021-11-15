#!/usr/bin/python3
import os
import cgi
import json
import logging 
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import cgitb
from http import cookies
from db_handler import Database


cgitb.enable()

logger = logging.getLogger()

database = Database.instance()
response = {"success": False}

form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

try:
    if os.environ['REQUEST_METHOD'] == 'POST':
        if 'HTTP_COOKIE' in os.environ:
            cookie = cookies.SimpleCookie(os.environ['HTTP_COOKIE'])
            if cookie is None:
                logger.exception('No tengo cookie')
             
            cookie_key = cookie.get('session_key').value
            cookie_value = cookie.get('session_value').value

            if database.check_credentials(cookie_key, cookie_value):
                if not database.exists_cookie(cookie_key, cookie_value):
                    logger.exception('No hay cookie, inserto una')
                    database.insert_cookie(cookie_key, cookie_value)
                else:
                    logger.exception('Tengo cookie')
                    cookie = database.get_cookie(cookie_key)
                response = {"success": True}
            else:
                logger.exception('Aqui Falla xq no coinciden las credenciales.')
        else:
            logger.exception('No vino cookie en el environment.')
except:
    response = {"success": False, "falla": "try"}    

print('Content-Type: application/json;charset=utf-8')
print()
logger.exception(response)
logger.exception(json.JSONEncoder().encode(response))
print(json.JSONEncoder().encode(response))
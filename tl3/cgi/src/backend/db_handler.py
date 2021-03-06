#!/usr/bin/python3
import os
import cgi
from http import cookies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, String, Integer, MetaData, DateTime, ForeignKey, tuple_
import logging


logger = logging.getLogger()

class Database:
    __instance = None

    @staticmethod
    def instance():
        if (Database.__instance == None):
            Database.__instance = Database()
        return Database.__instance

    def __init__(self):
        if (Database.__instance is not None):
            return Database.__instance
        db_string = "postgresql://admin:admin@tl3_db:5432/tl3"
        self.db = create_engine(db_string, echo=False)
        self.meta = MetaData(self.db)

        self.cookies = Table(
                        'cookies', 
                        self.meta, 
                        Column('key', String, primary_key=True),
                        Column('value', String)
                       )

        self.users = Table(
                        'users',
                        self.meta,
                        Column('id', Integer, primary_key=True),
                        Column('username', String),
                        Column('name', String),
                        Column('edad', Integer),
                        Column('sexo', Integer),
                        Column('password', String),
                        Column('fecha', Integer),
                        )

    def exists_cookie(self, key, value):
        result = self.meta.tables["cookies"]
        cookie_row = result.select().where(result.c.key==key)
        cookies_rs = self.db.execute(cookie_row)
        return cookies_rs.rowcount == 1

    def get_cookie(self, key):
        result = self.meta.tables["cookies"]
        cookie_row = result.select().where(result.c.key==key)
        cookie_rs = self.db.execute(cookie_row)
        if (cookie_rs.rowcount != 0):
            cookie = cookie_rs.first()
            return [cookie[0],cookie[1]]
        else:
            return []

    def insert_cookie(self, key, value):
        statement = self.cookies.insert().values(key=key, value=value)
        self.db.execute(statement)

    def check_credentials(self, username, password):
        result = self.meta.tables["users"]
        user_row = result.select().where(result.c.username == username).where(result.c.password == password)
        user_rs = self.db.execute(user_row)
        return user_rs.rowcount == 1

    def get_user_id_by_username(self, username):
        result = self.meta.tables["users"]
        user_row = result.select().where(result.c.username == username)
        user_rs = self.db.execute(user_row)
        if user_rs.rowcount == 1:
            user = user_rs.first().select(user_rs.c.id)
            return user
        else:
            return None
#!/usr/bin/python3
import cgi, cgitb
from http import cookies
import os
from db_handler import Database
import logging
import json

cgitb.enable()

if __name__ == "__main__" :
    print("Content-Type: application/json;charset=utf-8")
    print()
    print(json.JSONEncoder().encode('{"success": true}'))
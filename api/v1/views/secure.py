#!/usr/bin/python3
"""
secure the api using simple authentication
"""
from . import User, storage
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
from flask import g


@auth.verify_password
def verify_password(username, password):
    user = storage.get(User, None, username)

    if user is None:
        return False
    
    if user.password == password or user.confirm_pwd(password):
        g.user = user
        return True
    return False

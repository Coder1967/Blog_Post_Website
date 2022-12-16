#!/usr/bin/python3
"""
definition of blueprint to handle
functionalities involving user aithentication
"""
from flask import Blueprint

auth_print = Blueprint('auth_print', __name__, static_folder='auth_static',
                       template_folder='auth_templates')

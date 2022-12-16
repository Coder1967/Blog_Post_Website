#!/usr/bin/python3
"""
definition of blueprint to handle
functionalities not involving user aithentication     """
from flask import Blueprint


main_print = Blueprint('main_print', __name__, static_folder='main_static',
                       template_folder='main_templates')

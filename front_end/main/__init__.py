#!/usr/bin/python3
"""
definition of blueprint to handle
functionalities not involving user aithentication
"""
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import storage
from uuid import uuid4


main_print = Blueprint('main_print', __name__, static_folder='main_static',
                       template_folder='main_templates', url_prefix='/main')


@main_print.route('/home', strict_slashes=False)
@login_required
def home():
    """
    user homepage
    """
    posts = storage.all("Post")
    return render_template('home.html', posts=posts, user=current_user, cache_id=str(uuid4()))

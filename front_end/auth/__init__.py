#!/usr/bin/python3
"""
definition of blueprint to handle
functionalities involving user aithentication
"""
from uuid import uuid4
from flask import Blueprint, render_template, request
from flask import redirect, flash, url_for
from models import storage
from models.user import User
from flask_login import login_user, logout_user, login_required


auth_print = Blueprint('auth_print', __name__, static_folder='auth_static',
                       template_folder='auth_templates', url_prefix="/auth")


@auth_print.route("/signup", strict_slashes=False)
def signup():
    """
    adds a new user to the database
    """
    return render_template('signup.html', cache_id=str(uuid4()))


@auth_print.route("/login", strict_slashes=False)
def login():
    """
    webpage for logging in
    """
    return render_template('login.html', cache_id=str(uuid4()))


@auth_print.route("/login", methods=['POST'], strict_slashes=False)
def login_post():
    """
    logs a user in
    """
    name = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = storage.get(User, None, name)

    if not user or not user.confirm_pwd(password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth_print.login')) # if the user doesn't exist or password is wrong, reload the page

    login_user(user, remember=remember)
    return redirect(url_for('main_print.home'))


@auth_print.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_print.login'))

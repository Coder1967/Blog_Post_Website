#!/usr/bin/python3
"""
definition of blueprint to handle
functionalities not involving user aithentication
"""
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import storage
from uuid import uuid4
from models.user import User


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


@main_print.route('/<user_id>/profile', strict_slashes=False)
@login_required
def profile_page(user_id):
    """
    displays profile page
    """
    user = current_user
    profile_owner = storage.get(User, user_id)
    num = 0

    for post in user.posts:
        num += len(post.votes) 

    return render_template('profile_page.html', post_number=len(user.posts), user=user,
                            cache_id=str(uuid4()), vote_number=num, profile_id=profile_owner.id)


@main_print.route('/update_profile', strict_slashes=False)
@login_required
def update():
    """
    page that updates current user's profile
    """
    return render_template('update_profile.html', user=current_user, cache_id=str(uuid4()))

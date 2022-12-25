#!/usr/bin/python3
"""
definition of blueprint to handle
functionalities not involving user aithentication
"""
from flask import Blueprint, abort, render_template
from flask_login import login_required, current_user
from models import storage
from models.post import Post
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
    
    if profile_owner is None:
        abort(404)

    for post in profile_owner.posts:
        num += len(post.votes) 

    return render_template('profile_page.html', post_number=len(profile_owner.posts), user=user,
                            cache_id=str(uuid4()), vote_number=num, owner=profile_owner)


@main_print.route('/update_profile', strict_slashes=False)
@login_required
def update():
    """
    page that updates current user's profile
    """
    return render_template('update_profile.html', user=current_user, cache_id=str(uuid4()))



@main_print.route('/create_post', strict_slashes=False)
@login_required
def create_post():
    """
    page that create a blog post current user's account
    """
    return render_template('create_post.html', user=current_user, cache_id=str(uuid4()))


@main_print.route('/<post_id>/display_post', strict_slashes=False)
@login_required
def display_post(post_id):
    """
    page to display post
    """
    post = storage.get(Post, post_id)
    if post is None:
        abort(404)

    i = 0
    comment_dates = []
    post_votes = len(post.votes)
    created_at =  post.created_at.strftime("%m/%d/%Y")
    updated_at = post.updated_at.strftime("%m/%d/%Y")
    post_comments = len(post.comments)

    for comment in post.comments:
        comment_dates.append(comment.created_at.strftime("%m/%d/%Y"))

    return render_template('display_posts.html', post=post, user=current_user, cache_id=str(uuid4()), created_at=created_at,
            updated_at=updated_at, post_votes=post_votes, post_comments=post_comments,
            comment_dates=comment_dates)


@main_print.route('<user_name>/user_posts', strict_slashes=False)
@login_required
def user_posts(user_name):
    """
    display a user's posts
    """
    user = storage.get(User, None, user_name)
    posts = user.posts

    return render_template('user_posts.html', posts=posts, user=current_user, cache_id=str(uuid4()))

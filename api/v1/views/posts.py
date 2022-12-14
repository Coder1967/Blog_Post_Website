#!/usr/bin/python3
from . import storage
from . import Post, User
from . import app_views
from flask import abort, jsonify, request, current_app, g
with current_app.app_context():
    from .secure import auth, verify_password


@app_views.route('/users/<user_id>/posts', methods=['GET', 'POST'], strict_slashes=False)
def user_posts(user_id):
    """ GET: gets all posts by a user
        POST: adds a new post from a user"""

    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    if request.method == 'GET':
        posts = []

        for post in user.posts:
            posts.append(post.to_dict())
        return jsonify(posts)
    
    else:
        req = request.get_json()
        
        if req is None:
            abort(400, description="Not a json")
        if req.get('title') is None:
            abort(400, description='Missing title')
        if req.get('content') is None:
            abort(400, description='Missing content')
        if req.get('id'):
            del req['id']

        req['user_id'] = user_id
        post = Post(**req)
        post.save()
        return jsonify(post.to_dict()), 201


@app_views.route('posts/<post_id>', methods=['GET'], strict_slashes=False)
def get(post_id):
    """
    GET:gets a post using its id
    """
    post = storage.get(Post, post_id)
    if post is None:
        abort(404)
    return jsonify(post.to_dict())



@app_views.route('posts/<post_id>', methods=['DELETE', 'PUT'],
                 strict_slashes=False)
@auth.login_required
def post(post_id):
    """DELETE: deletes a post, PUT: updates a post"""
    post = storage.get(Post, post_id)
    if post is None:
        abort(404)

    """ 
    making sure only the owner of the post is allowed
    access to these http methods
    """
    if g.user.name != post.poster.name:
        abort(401)

    if request.method == 'PUT':
        post = storage.get(Post, post_id)
        restricted_attr = ['id', 'created_at', 'updated_at']
        req = request.get_json()

        if req is None:
            abort(400, description="Not a json")

        for key in req.keys():
            if key not in restricted_attr:
                setattr(post, key, req[key])
        post.save()
        post_dict = post.to_dict()
        del post_dict['poster']

        return jsonify(post_dict), 201

    else:
        storage.delete(post)
        storage.save()
        return jsonify({})


@app_views.route('/post_search', methods=['POST'],
           strict_slashes=False)
def search_post():
    """ searches for a post using query given"""
    req = request.get_json()
    posts = []

    if req is None:
        abort(400, description='Not a json')
    if req.get('query') is None:
        abort(400, description='Missing query')
    for post in storage.all(Post).values():
        if req['query'].lower() in post.title.lower():
            posts.append(post.to_dict())
    return jsonify(posts)

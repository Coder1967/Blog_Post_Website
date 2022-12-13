#!/usr/bin/python3
from . import storage
from . import Post, Comment, User
from . import app_views
from flask import abort, jsonify, request


@app_views.route('/posts/<post_id>/comments',
                 methods=['GET'], strict_slashes=False)
def get_comment(post_id):
    post = storage.get(Post, post_id)
    posts = []

    if post is None:
        abort(404)
    
    for comment in post.comments:
        posts.append(comment.to_dict())
    return jsonify(posts)


@app_views.route('/posts/<post_id>/<user_id>/comments',
                 methods=['POST'], strict_slashes=False)
def user_comment(post_id, user_id):
    """
    adds a new comment by a user to a post
    """
    post = storage.get(Post, post_id)
    req = request.get_json()
    user = storage.get(User, user_id)

    if user is None or post is None:
        abort(404)
    if req is None:
        abort(400, description="Not a json")
    if req.get("content") is None:
        abort(400, description="Missing content")

    req['user_id'] = user_id
    req['post_id'] = post_id
    comment = Comment(**req)
    comment.save()
    return jsonify(comment.to_dict())


@app_views.route('comments/<comment_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def comment(comment_id):
    """GET:gets a comment using its id, DELETE: deletes a comment, PUT: updates a comment"""
    comment = storage.get(Comment, comment_id)
    if comment is None:
        abort(404)

    if request.method == "GET":
        return jsonify(comment.to_dict())

    elif request.method == 'PUT':
        restricted_attr = ['id', 'created_at', 'updated_at']
        req = request.get_json()

        if req is None:
            abort(400, description="Not a json")
        if req.get('content') is None:
            abort(400, description='Missing content')

        for key in req.keys():
            if key not in restricted_attr:
                setattr(comment, key, req[key])
        comment.save()
        return jsonify(comment.to_dict()), 201

    else:
        storage.delete(comment)
        storage.save()
        return jsonify({})

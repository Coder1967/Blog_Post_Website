#!/usr/bin/python3
from . import storage
from . import Post, Comment
from . import app_views
from flask import abort, jsonify, request


@app_views.route('/Posts/<Post_id>/comments', methods=['GET', 'POST'], strict_slashes=False)
def post_comments(post_id):
    """ GET: gets all comments in a post
        POST: adds a new comment of a user to a post"""

    post = storage.get(Post, post_id)
    if post is None:
        abort(404)

    if request.method == 'GET':
        comments = []

        for comment in post.comments:
            comments.append(comment.to_dict)
        return jsonify(comments)
    
    else:
        req = request.get_json()
        
        if req is None:
            abort(400, description="Not a json")
        if req.get('content') is None:
            abort(400, description='Missing content')
        if req.get('id'):
            del req['id']

        req['post_id'] = post_id
        req['user_id'] = post.user_id
        comment = Comment(**req)
        comment.save()
        return jsonify(comment.to_dict()), 201


@app_views.route('comment/<comment_id>', methods=['GET', 'DELETE', 'PUT'],
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

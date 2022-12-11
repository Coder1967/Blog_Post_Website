#!/usr/bin/python3
from . import storage
from . import Post
from . import app_views
from flask import abort, jsonify, request

@app_views.route('/users/user_id/posts', methods=['GET', 'POST'], strict_slashes=False)
def post_user(user_id):
    if request.method == 'GET':
        user = storage.get(user_id)
        posts = []

        for post in user.posts:
            posts.append(post.to_dict)
        return jsonify(posts)
    
    else:
        req = request.get_json()
        
        if req is None:
            abort(400, description="Not a json")
        if req.get('title') is None:
            abort(400, description='Missing title')
        if req.get('content') is None:
            abort(400, description='Missing post')
        if req.get('post.id') is not None:
            del req['post.id']

        req['user_id'] = user_id
        post = Post(**req)
        post.save()

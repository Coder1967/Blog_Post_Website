#!/usr/bin/python3
"""api to interact with the users table"""
from . import User
from . import storage
from flask import jsonify, request, abort
from . import app_views


@app_views.route("/users", methods=['GET', 'POST'],
                 strict_slashes=False)
def get_and_post_users():
    """ 
    GET: returns all users.
    POST: creates and saves a new user
    """
    if request.method == "GET":
        users = []

        for user in storage.all(User).values():
            users.append(user.to_dict())
        return jsonify(users)

    else:
        req = request.get_json()
        user = object

        if req is None:
            abort(400, description="Not a json")
        if req.get('name') is None:
            abort(400, description="Missing name")
        if storage.get(User, None, req['name']):
            abort(400, description="Username is in use")
        if req.get("email") is None:
            abort(400, description="Missing email")
        if req.get("password") is None:
            abort(400, description="Missing password")
        if req.get("id"):
            del req['id']

        user = User(**req)
        user.save()
        return jsonify(user.to_dict), 201


@app_views.route('/users/user_id', methods=["PUT", "DELETE"],
                 strict_slashes=False)
def protected_user_methods(user_id):
    """
    PUT: updates user information
    DELETE: deletes user account
    """
    if request.method == 'PUT':
        user = storage.get(User, user_id)
        restricted_attr = ['id', 'created_at', 'updated_at']
        req = request.get_json()

        if user is None:
            abort(404)
        if req is None:
                abort(400, description="Not a json")
        for key in req.keys():
            if key not in restricted_attr:
                setattr(user, key, req[key])
        user.save()
        return jsonify(user.to_dict()), 201

    else:
        user = storage.get(User, user_id)
        if user is None:
            abort(404)
        else:                                                 storage.delete(user)
        storage.save()
        return jsonify({})


@app_views("/users/user_id", methods=["GET"], strict_slashes=False)
def get_user(user_id):
    """
    Get: returns a user in JSON format
    """
    user = storage.get(User, user_id)
    
    if user is None:
        abort(404)
    return jsonify(user.to_dict())

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
        if req.get("email") is None:
            abort(400, description="Missing email")
        if req.get("password") is None:
            abort(400, description="Missing password")
        if req.get("id"):
            del req['id']

        user = User(**req)
        user.save()
        return jsonify(user.to_dict), 201

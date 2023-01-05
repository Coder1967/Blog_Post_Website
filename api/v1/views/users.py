#!/usr/bin/python3
"""api to interact with the users table"""
from . import User
from . import storage
from flask import jsonify, request, abort, current_app, g
from . import app_views
import os
from werkzeug.utils import secure_filename
with current_app.app_context():
    from .secure import auth, verify_password



@app_views.route("/users/<user_id>", methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """
    Get: returns a user in JSON format
    """
    user = storage.get(User, user_id)

    if user is None:
        abort(404)
    return jsonify(user.to_dict())


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

        if req is None:
            abort(400, description="Not a json")
        if req.get('name') is None:
            abort(400, description="Missing name")
        if storage.get(User, None, req['name']):
            abort(400, description="Username is in use")
        if req.get("password") is None:
            abort(400, description="Missing password")
        if req.get("confirm_password") is None:
            abort(400, description="Fill out the confirm password field")
        if req['password'] != req['confirm_password']:
            abort(400, 'password does not match confirm password')

        if len(req["password"]) < 6:
            abort(400, "password must be at least 6 characters")
        if req.get("id"):
            del req['id']
        del req['confirm_password']

        user = User(**req)
        user.save()
        return jsonify(user.to_dict()), 201



@app_views.route('/users/<user_id>', methods=["PUT", "DELETE"],
                 strict_slashes=False)
@auth.login_required
def protected_user_methods(user_id):
    """
    PUT: updates user information
    DELETE: deletes user account
    """
    user = storage.get(User, user_id)
    if user is None:
            abort(404)

    """ ensuring only the owner of the account has access """
    if user.name != g.user.name:
        abort(401)

    if request.method == 'PUT':
        restricted_attr = ['id', 'created_at', 'updated_at']
        req = request.get_json()

        if req is None:
                abort(400, description="Not a json")
        if req['password'] != req['confirm_password']:
            abort(400, 'password does not match confirm password')
        for key in req.keys():
            if key not in restricted_attr:
                """ making sure password is hashed"""
                if key == 'password':
                     setattr(user, key, user.secure_password(req[key]))
                 else:
                    setattr(user, key, req[key])
        user.save()
        return jsonify(user.to_dict()), 201

    else:
        """ deleting profile picture before deleting user's account"""
        profile_pic = user.profile
        storage.delete(user)
        storage.save()
        cwd = os.getcwd()
        location = cwd + '/front_end/main/main_static/images/profile/' + user.profile
        if  profile_pic != 'default.jpg':
            os.remove(location)
        return jsonify({})

#!/usr/bin/python3
"""api to interact with the users table"""
from . import User
from . import storage
from flask import jsonify, request, abort, current_app
from . import app_views
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/vagrant/Blog_Post_Website/profile'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
current_app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

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
        if req.get("id"):
            del req['id']

        user = User(**req)
        user.save()
        return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=["PUT", "DELETE"],
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
        else:
            storage.delete(user)
        storage.save()
        return jsonify({})


@app_views.route("/users/<user_id>", methods=["POST"], strict_slashes=False)
def upload(user_id):
    """
    POST: uploads a file
    """
    user = storage.get(User, user_id)

    if user is None:
        abort(404)
    if 'file' not in request.files:
            abort(400, description='No file part')
    file = request.files['file']
    if file.filename == '':
        abort(400, description='No selected file')
    if file and allowed_file(file.filename):
        """ saving the file as well as updating the profile column to point to the file"""
        filename = user.name +'-' + user.id + "."
        filename += file.filename.split('.')[-1].lower()
        user.profile = filename
        user.save()
        file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))


def allowed_file(filename):
    """ checks if the file to be uploaded is of the right type"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

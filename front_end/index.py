#!/usr/bin/python3
"""
module to hold the Flask object
"""
from flask import Flask, redirect, url_for, request, abort
from .auth import auth_print
from .main import main_print
from flask_login import LoginManager
from models.user import User
from models import storage
import os


app = Flask(__name__)

app.register_blueprint(auth_print)
app.register_blueprint(main_print)
app.config['SECRET_KEY'] = 'tryegdrhghsgdufgdbdh32'
UPLOAD_FOLDER = os.getcwd() + '/front_end/main/main_static/images/profile'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config['MAX_CONTENT_PATH'] = 1000000


login_manager = LoginManager()
login_manager.login_view = 'auth_print.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """since the user_id is just the primary key of our user table, use it in the query for the user"""
    return storage.get(User, user_id)


@app.route("/users/<user_id>", methods=["POST"], strict_slashes=False)
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
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return redirect(url_for('main_print.profile_page', user_id=user.id))
    return "failed"

def allowed_file(filename):
    """ checks if the file to be uploaded is of the right type"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0", threaded=True)

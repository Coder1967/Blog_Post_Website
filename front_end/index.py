#!/usr/bin/python3
"""
module to hold the Flask object
"""
from flask import Flask
from .auth import auth_print
from .main import main_print
from flask_login import LoginManager
from models.user import User
from models import storage


app = Flask(__name__)

app.config['SECRET_KEY'] = 'tryegdrhghsgdufgdbdh32'

app.register_blueprint(auth_print)
app.register_blueprint(main_print)


login_manager = LoginManager()
login_manager.login_view = 'auth_print.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    """since the user_id is just the primary key of our user table, use it in the query for the user"""
    return storage.get(User, user_id)

if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0", threaded=True)

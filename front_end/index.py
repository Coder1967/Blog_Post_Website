#!/usr/bin/python3
"""
module to hold the Flask object
"""
from flask import Flask
from auth import auth_print
from main import main_print

app = Flask(__name__)
app.register_blueprint(auth_print)
app.register_blueprint(main_print)

if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0", threaded=True)

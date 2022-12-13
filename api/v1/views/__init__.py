#!/usr/bin/python3
from flask import Blueprint, current_app

app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')


from .users import UPLOAD_FOLDER
current_app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
from models import storage
from models.comment import Comment
from models.post import Post
from models.user import User
from models.vote import Vote

from .users import *
from .index import *
from .posts import *

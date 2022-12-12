#!/usr/bin/python3
from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')

from models import storage
from models.comment import Comment
from models.post import Post
from models.user import User
from models.vote import Vote
from .index import *
from .posts import *

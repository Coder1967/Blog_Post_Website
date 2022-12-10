#!/usr/bin/python3

from models.comment import Comment
from models.post import Post
from models.vote import Vote
from models.user import User
from models import storage

"""creation of needed objects"""
kwargs = {'name': "james", 'email':"james@gmail.com", 'password': "jamespwd"}
user = User(**kwargs)

kwargs = {'title': 'testing', 'content': 'contents of test', 'user_id': user.id}
post = Post(**kwargs)

kwargs = {'content': 'contents of test'}
comment = Comment(**kwargs)
""" unittests for database storage """


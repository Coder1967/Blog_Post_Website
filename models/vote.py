#!/usr/bin/python3
""" holds class Vote"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Storage
from models.comment import Comment
from models.post import Post

class Vote(BaseModel, Base):
    __tablename__ = 'votes'
    """definition of the Vote class"""
    post_id = Column(String(60), ForeignKey('posts.id'), nullable=True)
    comment_id = Column(String(60), ForeignKey('comments.id'), nullable=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=True)

    def __init__(self, *args, **kwargs):
        """initialization of a vote object"""
        super().__init__(self, *args, **kwargs)

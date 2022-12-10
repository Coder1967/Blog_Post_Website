#!/usr/bin/python3
""" holds class Vote"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Vote(BaseModel, Base):
    __tablename__ = 'votes'
    """definition of the Vote class"""
    post_id = Column(String(60), ForeignKey('posts.id'), nullable=False)
    comment_id = Column(String(60), ForeignKey('comments.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initialization of a vote object"""
        super().__init__(self, *args, **kwargs)

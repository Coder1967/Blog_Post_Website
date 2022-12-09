#!/usr/bin/python3

from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel

class Post(BaseModel, Base):
    """ defines the post object """
    __tablename__ = "posts"

    title = Column(String(70), nullable=False)
    comments = relationship("Comment", backref="post")
    votes = relationship("Vote", backref="post")
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=False)

    def __init__(self, *args, **kwargs):
        """ initialization of Post object"""
        super().__init__(*args, **kwargs)

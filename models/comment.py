#!/usr/bin/python3
""" module contains the Comment class"""

from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel

class Comment(BaseModel, Base):
    """ defines the comment class"""
    __tablename__ = "comments"

    content = Column(String(500), default="")
    post_id = Column(String(60), ForeignKey("posts.id"), nullable=True)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=True)
    votes = relationship("Vote", cascade = "all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """ initializes comment instance"""
        super().__init__(*args, **kwargs)


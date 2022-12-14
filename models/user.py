#!/usr/bin/python3
""" holds class User"""
import models
import hashlib
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from flask_login import UserMixin


location = "default.jpg"

class User(BaseModel, Base, UserMixin):
    """Representation of a user """
    __tablename__ = 'users'
    password = Column(String(128), nullable=False)
    profile = Column(String(120), default=location)
    name = Column(String(128), nullable=False, unique=True)
    votes = relationship("Vote", backref="voter", cascade = "all, delete, delete-orphan")
    posts = relationship("Post", backref="poster", cascade = "all, delete, delete-orphan")
    comments = relationship("Comment", backref="commenter",cascade = "all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        if kwargs.get('password') is not None:
            pwd = kwargs['password']
            del kwargs['password']
            self.secure_password(pwd)
        super().__init__(*args, **kwargs)

    def secure_password(self, pwd):
        """ encrypts user password to md5"""
        secure = hashlib.md5()
        secure.update(pwd.encode("utf-8"))
        self.password = secure.hexdigest()

    def confirm_pwd(self, pwd):
        """checks if password is correct"""
        secure = hashlib.md5()
        secure.update(pwd.encode("utf-8"))
        pwd = secure.hexdigest()
        if pwd == self.password:
            return True
        return False

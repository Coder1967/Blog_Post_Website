#!/usr/bin/python3
""" unnitests for the post module """
from unittest import TestCase
from models.post import Post
from models.base_model import BaseModel

kwargs = {'title': 'testing', 'content': 'contents of test'}
post = Post(**kwargs)

class TestPost(TestCase):
    """ beginning unittests """

    def test_title(self):
        """
        testing assignment of title attributes
        """
        self.assertEqual(post.title, 'testing')

    def test_str(self):
        """ makes sure the proper str representation is returned """
        string = "[Post] ({}) {}".format(post.id, post.__dict__)
        self.assertEqual(str(post), string)

    def test_isSubclass(self):
        """ checks if post is a subclass of BaseModel
        """
        self.assertIsInstance(post, BaseModel)

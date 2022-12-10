#!/usr/bin/python3
""" unnitests for the comment module """
from unittest import TestCase
from models.comment import Comment
from models.base_model import BaseModel

kwargs = {'content': 'contents of test'}
comment = Comment(**kwargs)

class TestComment(TestCase):
    """ beginning unittests """

    def test_content(self):
        """
        testing assignment of content attributes
        """
        self.assertEqual(comment.content, 'contents of test')

    def test_str(self):
        """ makes sure the proper str representation is returned """
        string = "[Comment] ({}) {}".format(comment.id, comment.__dict__)
        self.assertEqual(str(comment), string)

    def test_isSubclass(self):
        """ checks if comment is a subclass of BaseModel
        """
        self.assertIsInstance(comment, BaseModel)

#!/usr/bin/python3
""" unnitests for the vote module """
from unittest import TestCase
from models.vote import Vote
from models.base_model import BaseModel

vote = Vote()

class TestVote(TestCase):
    """ beginning unittests """

    def test_str(self):
        """ makes sure the proper str representation is returned """
        string = "[Vote] ({}) {}".format(vote.id, vote.__dict__)
        self.assertEqual(str(vote), string)

    def test_isSubclass(self):
        """ checks if comment is a subclass of BaseModel
        """
        self.assertIsInstance(vote, BaseModel)

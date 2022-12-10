#!/usr/bin/python3
""" unnitest for the user model """
from unittest import TestCase
from models.user import User
from models.base_model import BaseModel

kwargs = {'name': "james", 'email':"james@gmail.com", 'password': "jamespwd"}
user = User(**kwargs)

class test_user(TestCase):

    """ class to test the user model"""
    def test_confirm_pwd(self):
        """ testing if the 'confirm_password' method works as intended"""
        self.assertTrue(user.confirm_pwd('jamespwd'))

    def test_email(self):
        """ checks if the email public attr was properly assigned"""
        self.assertEqual(user.email, "james@gmail.com")

    def test_name(self):
        """ checks if the name public attr was properly assigned"""
        self.assertEqual(user.name, "james")

    def test_str(self):
        """ tests string representation"""
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), string)

    def test_to_dict(self):
        """ tests the to_dict function """
        dictionary = user.to_dict()

        usr2 = User(**dictionary)
        self.assertEqual(user.id, usr2.id)
        self.assertEqual(type(user), type(usr2))

    def test_issubclass(self):
        """ tests if User is a subclass of BaseModel"""
        self.assertIsInstance(user, BaseModel)

#!/usr/bin/python3
"""Defines unittests for models/user.py.
Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class Test_User(unittest.TestCase):
    """ Tests city """

    def test_pep8_User(self):
        """Tests pep8 style"""

        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "Check pep8")

    def test_save_updates_file(self):
        """Save files"""

        us = User()
        us.save()
        usid = "User." + us.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())

    def test_to_dict_output(self):
        """ Dictionary"""

        dt = datetime.today()
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
            }
        self.assertDictEqual(us.to_dict(), tdict)


if __name__ = "__main__":
    unittest.main()

#!/usr/bin/python3
""" Test review """

import unittest
from datetime import datetime
import pep8
import os
from models import Review
from models.base_model import BaseModel


class Test_Review(unittest.TestCase):
    """ Tests review """

    def test_pep8_City(self):
        """Tests pep8 style"""

        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "Check pep8")

    def test_save_updates_file(self):
        """Save """

        rv = Review()
        rv.save()
        rvid = "Review." + rv.id
        with open("file.json", "r") as f:
            self.assertIn(rvid, f.read())

    def test_to_dict_output(self):
        """Dictionary"""
        dt = datetime.today()
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(rv.to_dict(), tdict)


if __name__ = "__main__":
    unittest.main()

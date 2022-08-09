#!/usr/bin/python3
""" Test city """

from datetime import datetime
import unittests
import pep8
import os
from models import City
from models.base_model import BaseModel


class Test_City(unittest.TestCase):
    """ Tests city """

    def test_pep8_City(self):
        """Tests pep8 style"""

        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "Check pep8")

    def test_save_updates_file(self):
        """Test save"""

        cy = City()
        cy.save()
        cyid = "City." + cy.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())

    def test_to_dict_output(self):
        """Dict output"""

        dt = datetime.today()
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(cy.to_dict(), tdict)


if __name__ = "__main__":
    unittest.main()

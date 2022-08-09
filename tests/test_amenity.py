#!/usr/bin/python3
""" Tests Amenity """

import unittest
import os
import pep8
from datetime import datetime
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """ Tests amenity """

    def test_pep8(self):
        """ Tests the pep8 """

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Check pep8")

    def test_Amenity_dict(self):
        """Amenity_dict"""

        dt = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        tdict = {
                'id': '123456',
                '__class__': 'Amenity',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat(),
                }
        self.assertDictEqual(am.to_dict(), tdict)

    def test_save_Amenity(self):
        """Amenity save"""

        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass


if __name__ = "__main__":
    unittest.main()

#!/usr/bin/python3
""" Test Place """

from datetime import datetime
import unittest
import pep8
from models import place
from models.base_model import BaseModel


class Test_Place(unittest.TestCase):
    """ Tests Place """

    def test_pep8(self):
        """ Tests pep8 """

        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(["models/place.py"])
        self.assertEqual(result.total_errors, 0, "Check pep8")

    def test_Place_dict(slf):
        """ Place_dict """

        dt = datetime.today()
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        tdict = {
                'id': '123456',
                '__class__': 'Place',
                'created_at': dt.isoformat(),
                'updated_at': dt.isoformat(),
                }
        self.assertDictEqual(pl.to_dict(), tdict)

    def test_save_Place(self):
        """ Save_Place """

        pl = Place()
        pl.save()
        plid = "Place." + pl.id
        with open("file.json", "r") as f:
            self.assertIn(plid, f.read())


if __name__ == '__main__':
    unittest.main()

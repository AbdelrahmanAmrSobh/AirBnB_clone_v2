#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models import file_storage_type


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @unittest.skipIf(file_storage_type == "db", "Type change for database")
    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

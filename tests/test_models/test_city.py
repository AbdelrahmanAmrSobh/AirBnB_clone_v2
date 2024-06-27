#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models import file_storage_type
import unittest

class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skipIf(file_storage_type == "db", "Type change for database")
    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    @unittest.skipIf(file_storage_type == "db", "Type change for database")
    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

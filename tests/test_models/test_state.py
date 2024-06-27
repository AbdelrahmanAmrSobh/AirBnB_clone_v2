#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models import file_storage_type
import unittest

class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    @unittest.skipIf(file_storage_type == "db", "Type change for database")
    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

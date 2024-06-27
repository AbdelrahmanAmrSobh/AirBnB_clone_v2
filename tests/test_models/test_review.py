#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models import file_storage_type

class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    @test_basemodel.unittest.skipIf(file_storage_type == "db", "Type change for database")
    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    @test_basemodel.unittest.skipIf(file_storage_type == "db", "Type change for database")
    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    @test_basemodel.unittest.skipIf(file_storage_type == "db", "Type change for database")
    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

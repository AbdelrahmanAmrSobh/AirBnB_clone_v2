#!/usr/bin/python3
"""Test console"""

import unittest
import os
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
import models
import uuid
from models import storage, file_storage_type
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """class for testing"""

    Errors = {       
        "class_is_missing" : "** class name missing **",
        "class_not_found" : "** class doesn't exist **",
        "id_is_missing" : "** instance id missing **",
        "id_not_found" : "** no instance found **",
        "attribute_is_missing" : "** attribute name missing **",
        "value_is_missing" : "** value missing **"
    }

    @unittest.skipIf(file_storage_type == "db", "no need to set file if we don't use it")
    def setUp(self):
        """save old storage"""
        try:
            os.rename(os.getcwd() + "/file.json", "tmp_storage")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @unittest.skipIf(file_storage_type == "db", "no need to set file if we don't use it")
    def tearDown(self):
        """remove tmp storage"""
        try:
            os.remove(os.getcwd() + "/file.json")
        except IOError:
            pass
        try:
            os.rename(os.getcwd() + "/tmp_storage", "file.json")
        except IOError:
            pass

    def test_help(self):
        """test help"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        self.assertTrue(len(f.getvalue()) != 0)
        msg = "\nDocumented commands (type help <topic>):"
        self.assertTrue(f.getvalue().startswith(msg))

    def test_emptyline(self):
        """test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        self.assertEqual("", f.getvalue())

    def test_create(self):
        """
        test create, show, destroy, all and update with class name
        """
        classes = [" BaseModel ", " User ", " Place ", " State ",
                   " City ", " Amenity ", " Review "]
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create" + class_name)
                response = f.getvalue()
                for error in TestConsole.Errors.values():
                    self.assertNotEqual(response, error)
                    self.assertEqual(type(response), str)

    def test_storage(self):
        """
        test create, show, destroy, all and update with class name
        """
        classes = ["BaseModel", "User", "Place", "State",
                   "City", "Amenity", "Review"]
        for class_name in classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create " + class_name)
                response = f.getvalue()[:-1]
                key = f"{class_name}.{response}"
                self.assertIn(key, storage.all())

    def test_create_fail(self):
        """
        test create, show, destroy, all and update with class name
        """


        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create FakeClassNameThatShouldn'tExist")
            response = f.getvalue()[:-1]
            self.assertEqual(response, TestConsole.Errors['class_not_found'])

    def test_class_name_function(self):
        """
        test class name with all, count, show, destroy, update <attr> <value>
        and update <dict>.
        """
        classes = ["BaseModel", "User", "Place", "State",
                   "City", "Amenity", "Review"]
        pass


if __name__ == "__main__":
    unittest.main()
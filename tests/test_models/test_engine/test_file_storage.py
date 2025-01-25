#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models.city import City
# from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        self.storage = FileStorage()
        self.state = State(name="California")
        self.city = City(name="San Francisco")
        self.storage.new(self.state)
        self.storage.new(self.city)
        self.storage.save()

    def tearDown(self):
        """ Remove storage file at end of tests
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass
        del self.storage
        """

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        storage = FileStorage()
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        self.storage.new(new)
        self.assertIn(f"BaseModel.{new.id}", self.storage.all().keys())

    def test_all(self):
        """ __objects is properly returned """
        self.assertIsInstance(self.storage.all(), dict)

    def test_delete_existing_object(self):
        """ Test deleting an existing object """
        self.storage.delete(self.state)
        self.assertNotIn(f"State.{self.state.id}", self.storage.all())

    def test_delete_non_existing_object(self):
        """ Test deleting a non-existing object """
        dummy = BaseModel()
        initial_count = len(self.storage.all())
        self.storage.delete(dummy)
        self.assertEqual(len(self.storage.all()), initial_count)

    def test_delete_none(self):
        """ Test deleting when obj is None """
        initial_count = len(self.storage.all())
        self.storage.delete(None)
        self.assertEqual(len(self.storage.all()), initial_count)

    def test_all_no_class(self):
        """ Test all() with no class argument """
        objs = self.storage.all()
        self.assertIn(f"State.{self.state.id}", objs)
        self.assertIn(f"City.{self.city.id}", objs)

    def test_all_with_class(self):
        """ Test all() with a class argument """
        states = self.storage.all(State)
        self.assertIn(f"State.{self.state.id}", states)
        self.assertNotIn(f"City.{self.city.id}", states)

    def test_all_with_no_matching_class(self):
        """ Test all() with a class that has no instances """
        from models.user import User
        users = self.storage.all(User)
        self.assertEqual(len(users), 0)

    def test_save(self):
        """ FileStorage save method """
        self.storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        self.storage.save()
        self.storage.reload()
        objs = self.storage.all()
        self.assertIn(f"State.{self.state.id}", objs)
        self.assertIn(f"City.{self.city.id}", objs)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

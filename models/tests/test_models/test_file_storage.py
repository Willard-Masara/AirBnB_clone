import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up a test instance of the FileStorage class.
        """
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        """
        Clean up: delete the file after each test.
        """
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all_empty(self):
        """
        Test if all() returns an empty dictionary initially.
        """
        all_objects = self.storage.all()
        self.assertEqual(all_objects, {})

    def test_new(self):
        """
        Test if new() adds an object to __objects.
        """
        self.storage.new(self.base_model)
        all_objects = self.storage.all()
        key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.assertIn(key, all_objects)

    def test_save_and_reload(self):
        """
        Test if save() writes to file and reload() reads from file correctly.
        """
        self.storage.new(self.base_model)
        self.storage.save()

        # Create a new storage instance to simulate a different session
        new_storage = FileStorage()
        new_storage.reload()

        all_objects = new_storage.all()
        key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.assertIn(key, all_objects)
        reloaded_model = all_objects[key]
        self.assertEqual(reloaded_model.id, self.base_model.id)
        self.assertEqual(reloaded_model.created_at, self.base_model.created_at)
        self.assertEqual(reloaded_model.updated_at, self.base_model.updated_at)

    def test_reload_empty_file(self):
        """
        Test if reload() handles an empty file correctly.
        """
        self.storage.save()

        # Create a new storage instance to simulate a different session
        new_storage = FileStorage()
        new_storage.reload()

        all_objects = new_storage.all()
        self.assertEqual(all_objects, {})

    def test_reload_nonexistent_file(self):
        """
        Test if reload() handles a nonexistent file correctly.
        """
        self.storage._FileStorage__file_path = "nonexistent_file.json"
        self.storage.reload()

        all_objects = self.storage.all()
        self.assertEqual(all_objects, {})

    def test_reload_corrupted_file(self):
        """
        Test if reload() handles a corrupted file correctly.
        """
        with open(self.storage._FileStorage__file_path, 'w') as file:
            file.write("corrupted JSON data")

        self.storage.reload()

        all_objects = self.storage.all()
        self.assertEqual(all_objects, {})

if __name__ == '__main__':
    unittest.main()


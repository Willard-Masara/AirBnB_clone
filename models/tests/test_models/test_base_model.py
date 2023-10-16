import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up a test instance of the BaseModel class.
        """
        self.base_model = BaseModel()

    def test_id_is_string(self):
        """
        Test if the id attribute is a string.
        """
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """
        Test if created_at attribute is an instance of datetime.
        """
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        Test if updated_at attribute is an instance of datetime.
        """
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """
        Test if the save method updates the updated_at attribute.
        """
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_contains_keys(self):
        """
        Test if to_dict method returns a dictionary containing required keys.
        """
        keys = ['id', 'created_at', 'updated_at', '__class__']
        obj_dict = self.base_model.to_dict()
        for key in keys:
            self.assertIn(key, obj_dict)

    def test_to_dict_datetime_format(self):
        """
        Test if the datetime strings in the to_dict method are in the correct format.
        """
        obj_dict = self.base_model.to_dict()
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())

    def test_str_representation(self):
        """
        Test if the __str__ method returns the correct string representation.
        """
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_to_dict_includes_custom_attribute(self):
        """
        Test if a custom attribute is included in the dictionary representation.
        """
        self.base_model.custom_attr = "custom_value"
        obj_dict = self.base_model.to_dict()
        self.assertIn('custom_attr', obj_dict)

    def test_to_dict_excludes_private_attribute(self):
        """
        Test if private attributes are excluded from the dictionary representation.
        """
        self.base_model._private_attr = "private_value"
        obj_dict = self.base_model.to_dict()
        self.assertNotIn('_private_attr', obj_dict)

    def test_recreate_instance_from_dict(self):
        """
        Test if a BaseModel instance can be recreated from its dictionary representation.
        """
        original_model_dict = self.base_model.to_dict()
        recreated_model = BaseModel(**original_model_dict)
        self.assertEqual(recreated_model.id, self.base_model.id)
        self.assertEqual(recreated_model.created_at, self.base_model.created_at)
        self.assertEqual(recreated_model.updated_at, self.base_model.updated_at)

if __name__ == '__main__':
    unittest.main()


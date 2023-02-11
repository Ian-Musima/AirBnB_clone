from models.base_model import BaseModel
import unittest
from datetime import datetime
import time

class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        """
        Test that BaseModel creates an instance
        and that its attributes are of the correct type.
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertIsInstance(instance.id, str)

    def test_save(self):
        """
        Tests that the save method of the BaseModel class
        updates the updated_at
        """
        instance = BaseModel()
        time.sleep(0.000000000000001)
        instance.save()
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertIsInstance(instance.id, str)
        self.assertNotEqual(instance.created_at, instance.updated_at)

    def test_string_representation(self):
        """
        Test the string representation of the BaseModel instance
        """
        instance = BaseModel()
        instance_string = instance.__str__()
        test_string = f"[{instance.__class__.__name__}] {(instance.id)} {instance.__dict__}"
        self.assertEqual(instance_string, test_string)

    def test_dictionary_representation(self):
        """
        Tests that the to_dict method of the BaseModel class
        returns a dictionary in the expected format
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIsInstance(instance_dict["id"], str)
        self.assertIsInstance(instance_dict["updated_at"], str)
        self.assertIsInstance(instance_dict["created_at"], str)
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        



if __name__ == '__main__':
    unittest.main()
import unittest
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestState(unittest.TestCase):
    def test_state_inherits_from_base_model(self):
        # Test if State class inherits from BaseModel
        state = State()
        self.assertIsInstance(state, BaseModel)
        # Add more tests for State class attributes and methods

class TestCity(unittest.TestCase):
    def test_city_inherits_from_base_model(self):
        # Test if City class inherits from BaseModel
        city = City()
        self.assertIsInstance(city, BaseModel)
        # Add more tests for City class attributes and methods

class TestAmenity(unittest.TestCase):
    def test_amenity_inherits_from_base_model(self):
        # Test if Amenity class inherits from BaseModel
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        # Add more tests for Amenity class attributes and methods

class TestPlace(unittest.TestCase):
    def test_place_inherits_from_base_model(self):
        # Test if Place class inherits from BaseModel
        place = Place()
        self.assertIsInstance(place, BaseModel)
        # Add more tests for Place class attributes and methods

class TestReview(unittest.TestCase):
    def test_review_inherits_from_base_model(self):
        # Test if Review class inherits from BaseModel
        review = Review()
        self.assertIsInstance(review, BaseModel)
        # Add more tests for Review class attributes and methods

if __name__ == "__main__":
    unittest.main()


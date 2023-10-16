#!/usr/bin/python3
from models.base_model import BaseModel

"""
Thisis the class for adding amenities
"""


class Amenity(BaseModel):
    """
    Amenity class inherits from BaseModel.
    Public class attributes:
        name: string - empty string
    """
    name = ""
    
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the Amenity class.
        """
        super().__init__(*args, **kwargs)


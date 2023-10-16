#!/usr/bin/python3
from models.base_model import BaseModel

"""
THis is the class for reviews
"""


class Review(BaseModel):
    """
    Review class inherits from BaseModel.
    Public class attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the Review class.
        """
        super().__init__(*args, **kwargs)


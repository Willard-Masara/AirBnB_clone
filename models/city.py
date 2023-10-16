#!/usr/bin/python3
from models.base_model import BaseModel

"""
This is the class fpor adding the city
"""


class City(BaseModel):
    """
    City class inherits from BaseModel.
    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
    
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the City class.
        """
        super().__init__(*args, **kwargs)


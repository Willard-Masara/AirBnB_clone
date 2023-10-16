#!/usr/bin/python3
from models.base_model import BaseModel

"""
THis is thew class for the satge
"""


class State(BaseModel):
    """
    State class inherits from BaseModel.
    Public class attributes:
        name: string - empty string
    """
    name = ""
    
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the State class.
        """
        super().__init__(*args, **kwargs)


#!/usr/bin/python3
import uuid
from datetime import datetime
import models

"""
This is the superclass from whence all child classes will grow
"""


class BaseModel:
    """
    BaseModel class represents the base model for other classes.

    Attributes:
        id (str): Unique identifier for the instance.
        created_at (datetime): Timestamp representing the creation time.
        updated_at (datetime): Timestamp representing the last update time.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        If kwargs is provided, sets attributes based on the key-value pairs in kwargs.
        If kwargs is empty, creates new id and created_at attributes.

        Args:
            *args: Not used.
            **kwargs: Dictionary containing attribute names and values.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)

            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the object attributes to a dictionary for serialization.

        Returns:
            dict: A dictionary containing object attributes.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: String representation of the object.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def  save(self):
        """
        Saves the object to the storage
        """
        storage.new(self)
        storage.save()


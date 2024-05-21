#!/usr/bin/python3
"""
base model for the airbnb clone
"""

from datetime import datetime, timedelta
import uuid


class BaseModel:
    """
    A base class for other classes in the project.

    Attributes:
        id (str): Unique identifier for the instance, assigned as a UUID string.
        created_at (datetime): The datetime when the instance is created.
        updated_at (datetime): The datetime when the instance is last updated.

    Methods:
        __str__(self): Returns a string representation of the instance.
        save(self): Updates the updated_at attribute with the current datetime.
        to_dict(self): Returns a dictionary representation of the instance.
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the instance.

        The dictionary includes all attributes set on the instance, with the
        following modifications:
            - A '__class__' key is added with the class name of the object.
            - created_at and updated_at are converted to ISO format strings.
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict

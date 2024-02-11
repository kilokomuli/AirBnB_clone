#!/usr/bin/python3
"""Defines class Amenity that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class that defines properties of Amenity.

    Attributes:
        name (string): name of amenity.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of Amenity.
        """
        super().__init__(*args, **kwargs)

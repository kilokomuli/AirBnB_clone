#!/usr/bin/python3
"""Defines class review that inherits from BaseModel"""
from models.base_model import BaseModel


class Review (BaseModel):
    """Class that defines properties of Review .

    Attributes:
        place_id (string): id of city.
        user_id (string): id of user.
        text (string): just a text.
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of Review.
        """
        super().__init__(*args, **kwargs)

#!/usr/bin/python3
from models.base_model import BaseModel
"""Defines class User"""


class  User(BaseModel):
    """Class user that inherits from Basemodel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instance of user"""
        super().__init__(*args, **kwargs)

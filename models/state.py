#!/usr/bin/python3
from models.base_model import BaseModel
"""Defines class state inheriting from BaseModel"""


class State(BaseModel):
    """Defines properties of state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Creates new instances of State.
        """
        super().__init__(*args, **kwargs)

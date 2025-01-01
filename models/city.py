#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """The links to the cities table in the database"""
    state_id = ''
    name = ''

#!/usr/bin/python3

from models.base_model import BaseModel


class review(BaseModel):
    ''' creates the review class which inherits from the BaseModel'''
    
    place_id: str = ""
    user_id: str = ""
    text: str = ""
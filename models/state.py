#!/usr/bin/python

from models.base_model import BaseModel
'''imports the basemodel class'''


class state(BaseModel):
    '''creates the state clase which inherits the base model class'''
    
    name: str = ""

    def __init__(self):
    
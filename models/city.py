#!/usr/bin/python3
'''the city module'''

from models.base_model import BaseModel


class City(BaseModel):
    '''the city in the listing
    
    Attributes
        state_id
        name
    '''
    
    state_id = ""
    name = ""
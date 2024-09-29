#!/usr/bin/python3
'''the review module'''

from models.base_model import BaseModel


class Review(BaseModel):
    ''' The review(s) for a listing
     
    Attributes:
        text
        user_id
        place_id
     '''
    place_id = ""
    user_id = ""
    text = ""
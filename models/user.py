from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel"""
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   #Call the BaseModel initializer


    def __str__(self):
        return f"[User] ({self.id}) {{'email': '{self.email}', 'first_name': '{self.first_name}', 'last_name': '{self.last_name}'}}"

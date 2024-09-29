from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel"""
    
    def __init__(self, email="", password="", first_name="", last_name="", *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the BaseModel initializer
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"[User] ({self.id}) {{'email': '{self.email}', 'first_name': '{self.first_name}', 'last_name': '{self.last_name}'}}"

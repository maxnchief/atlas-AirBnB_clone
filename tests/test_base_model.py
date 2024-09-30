#!/usr/bin/python3
from models.base_model import BaseModel

# Create an instance of BaseModel
my_model = BaseModel()

# Assign some attributes to the instance
my_model.name = "My First Model"
my_model.my_number = 89

# Print the instance (uses __str__ method from BaseModel)
print(my_model)

# Save the instance (this will call the save method and update updated_at)
my_model.save()

# Print the instance again
print(my_model)

# Convert the instance to a dictionary
my_model_json = my_model.to_dict()

# Print the JSON representation
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(
        key, type(my_model_json[key]), my_model_json[key]
    ))

from typing import TypedDict


# TypedDict is used to define the expected structure of a dictionary
class Person(TypedDict):

    # 'name' must contain a string value
    name: str

    # 'age' must contain an integer value
    age: int


# Creating a dictionary according to the Person structure
new_person: Person = {
    "name": "Shubham",
    "age": 35
}


# Print the dictionary
print(new_person)
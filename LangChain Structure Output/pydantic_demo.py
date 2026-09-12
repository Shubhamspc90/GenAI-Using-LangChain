from pydantic import BaseModel, EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str = "Varun"
    age: Optional[int] = None
    email: EmailStr

new_student = {
    "age": "24",
    "email": "abc@gmail.com",
    'cgpa':12
}

student = Student(**new_student)

print(student)
print(student.age)
print(student.email)
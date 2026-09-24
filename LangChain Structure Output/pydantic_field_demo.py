from pydantic import BaseModel, Field
from typing import Optional


class Student(BaseModel):

    # ---------------- BASIC ----------------

    name: str = Field(
        default="Varun",                    # Default value
        description="Student's full name"   # Field ka description
    )

    age: int = Field(
        default=18,                         # Default value
        title="Student Age",                # Field ka title
        description="Age of the student"   # Field ka description
    )


    # ---------------- NUMBER VALIDATION ----------------

    marks: float = Field(
        default=0,
        gt=0,                               # Greater Than 0 → marks > 0
        ge=0,                               # Greater Than or Equal → marks >= 0
        lt=100,                             # Less Than 100 → marks < 100
        le=100,                             # Less Than or Equal → marks <= 100
        description="Student's marks"
    )


    # ---------------- STRING VALIDATION ----------------

    course: str = Field(
        default="Python",

        min_length=2,                       # Minimum 2 characters
        max_length=20,                      # Maximum 20 characters

        description="Course name"
    )


    # ---------------- OPTIONAL FIELD ----------------

    city: Optional[str] = Field(
        default=None,                       # Field optional hai
        description="Student's city"
    )


student = Student(
    name="Shubham",
    age=24,
    marks=85,
    course="Python",
    city="Delhi"
)

print(student)
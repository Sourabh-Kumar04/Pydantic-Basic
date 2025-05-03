from pydantic import BaseModel, Field
from typing import List, Dict, Optional

# TODO: Create Employee model with the following fields:
# - id (int)
# - name (str (min 3 characters))
# - department (optional str (default = "General"))
# - salary (float (must be greater than 10000))

class Employee(BaseModel):
    id : int
    name: str = Field(
        ...,
        min_length=3,
        description="Name of the employee, must be at least 3 characters long.",
        example="Sourabh Kumar"
    )
    department: Optional[str] = Field(
        default="General",
        description="Department of the employee, defaults to 'General' if not provided.",
        example="Engineering"
    )
    salary: float = Field(
        ...,
        gt=10000, 
        description="Salary of the employee, must be greater than 10000.",
        example=15000.0
    )
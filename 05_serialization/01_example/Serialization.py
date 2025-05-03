from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    country: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime("%d/%m%Y %H:%M:%S"),
        }
    )

# Crceate a user instance
user = User(
    id=1,
    name="Sourabh Kumar",
    email="sourabh@example.com",
    created_at=datetime.now(),
    address = Address(
        street="123 harban Singh Marg",
        city="New Delhi",
        state="Delhi",
        zip_code='110019',
        country="India"
    ),
    is_active = False,
    tags = ["premium", "verfied"]
)

# Using model_dump() -> dict
python_dict = user.model_dump()
print(python_dict)

print("\n")

# Using model_dump_json() -> JSON str
json_str = user.model_dump_json()
print(json_str)

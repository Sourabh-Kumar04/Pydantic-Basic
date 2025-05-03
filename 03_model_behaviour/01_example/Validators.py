from pydantic import BaseModel, Field, field_validator, model_validator, computed_field 

class User(BaseModel):
    username: str

    @field_validator('username')
    def check_username(cls, v):
        if len(v) <= 3:
            raise ValueError('Username must be longer than 3 characters')
        return v
    
class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def check_password(cls, values):
        if values['password'] != values['confirm_password']:
            raise ValueEror("Password do not match")
        return values

class Product(BaseModel):
    name: str
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
from pydantic import BaseModel, Field, field_validator, model_validator, computed_field

# TODO: Create Booking model
# Fields:
# - user_id: int
# - room_id: int
# - nights: int (must be greater than 0)
# - rate_per_night: float (must be greater than 1000)
# - Also, add computed fields: total_amount = nights * rate_per_night

class Booking(BaseModel):
    user_id: int
    room_id: int 
    nights: int = Field(
        ...,
        ge=1,
        description="Number of nights must be greater than 1"
    )
    rate_per_night: float = Field(
        ...,
        ge=1000,
        description='Rate per night mustbe greater than 0'
    )
    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night
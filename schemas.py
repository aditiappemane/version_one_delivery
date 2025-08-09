from typing import Optional, Annotated
from datetime import time, datetime
from pydantic import BaseModel, Field, StringConstraints, condecimal
from typing import Optional

# Common base schema for restaurant fields
class RestaurantBase(BaseModel):
    name: Annotated[str, StringConstraints(min_length=3, max_length=100)]
    description: Optional[str] = None
    cuisine_type: str
    address: str
    phone_number: Annotated[
        str,
        StringConstraints(pattern=r'^\+?\d{1,3}[- ]?\d{6,15}$')
    ]
    rating: condecimal(ge=0.0, le=5.0) = 0.0
    is_active: bool = True
    opening_time: time
    closing_time: time
    updated_at: Optional[datetime] = None


# Schema for creating a restaurant
class RestaurantCreate(RestaurantBase):
    pass


# Schema for updating a restaurant
class RestaurantUpdate(BaseModel):
    name: Optional[Annotated[str, StringConstraints(min_length=3, max_length=100)]] = None
    description: Optional[str] = None
    cuisine_type: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[
        Annotated[str, StringConstraints(pattern=r'^\+?\d{1,3}[- ]?\d{6,15}$')]
    ] = None
    rating: Optional[condecimal(ge=0.0, le=5.0)] = None
    is_active: Optional[bool] = None
    opening_time: Optional[time] = None
    closing_time: Optional[time] = None


# Schema for database response
class RestaurantInDBBase(RestaurantBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # For ORM mode in Pydantic v2


# Schema for API responses
class Restaurant(RestaurantInDBBase):
    pass


# Schema for internal DB operations (if needed)
class RestaurantInDB(RestaurantInDBBase):
    pass

class RestaurantOut(Restaurant):
    pass

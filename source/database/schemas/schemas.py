# This is the data validation class
# This represents the database representation

from datetime import datetime
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class UserResponse(BaseModel):
    id: int
    name: str
    phone_number: str

    model_config = {
        "from_attributes":True
    }

class UserCreate(BaseModel):
    id: int
    name: str

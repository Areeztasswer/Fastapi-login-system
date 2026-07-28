

from pydantic import BaseModel, Field, field_validator
from enum import Enum



class Product(BaseModel):
    Id: int = Field(gt=0)
    Name: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=5, max_length=200)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)


    
    @field_validator("Name")
    @classmethod
    def validate_name(cls, value):
        if not value.isalpha():
            raise ValueError("Product name should contain only letters.")
        return value.title()#title capitalizes the first letter of each word in the string
    
class Role(str, Enum):
    admin = "admin"
    employee = "employee"

class User(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    password: str = Field(min_length=6, max_length=8)
    role: Role
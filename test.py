from typing import List, Optional
from pydantic import BaseModel

class Identifier(BaseModel):
    system: str
    value: str

class Name(BaseModel):
    family: str
    given: List[str]

class Patient(BaseModel):
    resourceType: str = "Patient"
    identifier: List[Identifier]
    name: List[Name]
    birthDate: Optional[str]
    gender: Optional[str]
    address: Optional[List[str]]
    # Add any other fields as needed
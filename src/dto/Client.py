from pydantic import BaseModel

from .IdentifierType import IdentifierTypeResponse

from typing import Optional

class ClientRequest(BaseModel):
    id_identifier_type: str
    identifier: str
    name: str
    email: str
    password: str
    location: str
    credits: int

class ClientResponse(BaseModel):
    id: str
    identifier_type: IdentifierTypeResponse
    identifier: str
    name: str
    email: str
    password: str
    location: str
    credits: int

    class Config:
        orm_mode = True

class ClientUpdateRequest(BaseModel):
    id: str
    id_identifier_type: Optional[str]
    identifier: Optional[str]
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    location: Optional[str]
    credits: Optional[int]

    class Config:
        orm_mode = True
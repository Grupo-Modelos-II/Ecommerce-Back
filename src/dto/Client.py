from pydantic import BaseModel

from .IdentifierType import IdentifierTypeResponse

from typing import Optional

class ClientRequest(BaseModel):
    id: Optional[str] = None
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
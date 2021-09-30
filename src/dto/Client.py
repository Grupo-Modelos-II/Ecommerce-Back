from pydantic import BaseModel

from .IdentifierType import IdentifierTypeResponse

class ClientRequest(BaseModel):
    id_identifier_type: str
    identifier: str
    name: str
    email: str
    location: str
    credits: int

class ClientResponse(BaseModel):
    id: str
    identifier_type: IdentifierTypeResponse
    identifier: str
    name: str
    email: str
    location: str
    credits: int

    class Config:
        orm_mode = True
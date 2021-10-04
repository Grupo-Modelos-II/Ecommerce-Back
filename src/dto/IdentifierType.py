from typing import Optional

from pydantic import BaseModel

class IdentifierTypeRequest(BaseModel):
    name: str


class IdentifierTypeResponse(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True
from typing import Optional

from pydantic import BaseModel

class IdentifierTypeRequest(BaseModel):
    name: str


class IdentifierTypeResponse(IdentifierTypeRequest):
    id: str

    class Config:
        orm_mode = True
from typing import Optional

from pydantic import BaseModel

from typing import Optional

class IdentifierTypeRequest(BaseModel):
    id: Optional[str] = None
    name: str


class IdentifierTypeResponse(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True
from pydantic import BaseModel

from typing import Optional

class CategoryRequest(BaseModel):
    id: Optional[str] = None
    name: str

class CategoryResponse(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True
from pydantic import BaseModel

from .Category import CategoryResponse
from typing import Optional

class ProductRequest(BaseModel):
    name: str
    amount: int
    id_category: str
    description: str
    cost: int

class ProductResponse(BaseModel):
    id: str
    name: str
    amount: int
    mainImage: Optional[str]
    images: Optional[list[str]]
    category: CategoryResponse
    description: str
    cost: int

    class Config:
        orm_mode = True
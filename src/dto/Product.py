from pydantic import BaseModel, validator

from .Category import CategoryResponse
from typing import Optional

class ProductRequest(BaseModel):
    name: str
    amount: int
    id_category: str
    description: str
    cost: int


class ProductImage(BaseModel):
    id_product: str
    image: str

    class Config:
        orm_mode = True

class ProductResponse(BaseModel):
    id: str
    name: str
    amount: int
    mainImage: Optional[str]
    images: list[ProductImage]
    category: CategoryResponse
    description: str
    cost: int

    class Config:
        orm_mode = True
        validate_assignment = True

    @validator('mainImage')
    def set_mainImage(cls, mainImage):
        return mainImage or ''
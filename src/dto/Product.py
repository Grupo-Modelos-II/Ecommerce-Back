from pydantic import BaseModel, validator

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
        validate_assignment = True

    @validator('mainImage')
    def set_mainImage(cls, mainImage):
        return mainImage or ''

    @validator('images')
    def set_images(cls, images):
        return images or []
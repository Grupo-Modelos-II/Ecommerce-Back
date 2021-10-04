from pydantic import BaseModel

from .Category import CategoryResponse

class ProductRequest(BaseModel):
    name: str
    id_category: str
    description: str
    cost: int

class ProductResponse(BaseModel):
    id: str
    name: str
    category: CategoryResponse
    description: str
    cost: int

    class Config:
        orm_mode = True
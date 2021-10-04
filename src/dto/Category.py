from pydantic import BaseModel

class CategoryRequest(BaseModel):
    name: str

class CategoryResponse(CategoryRequest):
    id: int

    class Config:
        orm_mode = True
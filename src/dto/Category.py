from pydantic import BaseModel

class CategoryRequest(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True
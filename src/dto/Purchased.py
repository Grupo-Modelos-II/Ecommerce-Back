from pydantic import BaseModel
from .Product import ProductResponse

class PurchasedRequest(BaseModel):
    id_transaction: str
    id_product: str
    amount: int
    cost: int

class PurchasedResponse(BaseModel):
    id: str
    product: ProductResponse
    amount: int
    cost: int

    class Config:
        orm_mode = True
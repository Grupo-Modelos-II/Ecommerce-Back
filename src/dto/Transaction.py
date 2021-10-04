from pydantic import BaseModel
from datetime import date
from .Client import ClientResponse
from .Purchased import PurchasedResponse

class TransactionRequest(BaseModel):
    id_client: str
    total: int

class TransactionResponse(BaseModel):
    id: str
    client: ClientResponse
    purchases: list[PurchasedResponse]
    date: date
    total: int

    class Config:
        orm_mode = True
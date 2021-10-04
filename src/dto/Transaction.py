from pydantic import BaseModel
from datetime import date
from .Client import ClientResponse
from .Purchased import PurchasedResponse

from typing import Optional

class TransactionRequest(BaseModel):
    id: Optional[str] = None
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
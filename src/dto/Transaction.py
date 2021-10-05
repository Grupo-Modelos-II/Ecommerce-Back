from pydantic import BaseModel
from datetime import date
from .Client import ClientResponse
from .Purchased import PurchasedResponse
from typing import Optional

class TransactionRequest(BaseModel):
    id_client: str
    total: int

class TransactionUpdateRequest(BaseModel):
    id:str
    id_client:Optional[str]
    total:Optional[int]

class TransactionResponse(BaseModel):
    id: str
    client: ClientResponse
    purchases: list[PurchasedResponse]
    date: date
    total: int

    class Config:
        orm_mode = True
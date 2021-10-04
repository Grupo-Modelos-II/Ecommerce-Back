from pydantic import BaseModel
from datetime import date
from dto.Client import ClientResponse

class TransactionRequest(BaseModel):
    id_client: str
    date: date
    total: int

class TransactionResponse(BaseModel):
    id_transaction: str
    client: ClientResponse
    purchases: PurchasedResponse
    date: date
    total: int

    class Config:
        orm_mode = True
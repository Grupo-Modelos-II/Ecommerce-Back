from sqlalchemy.orm import Session
from dto.Purchased import PurchasedRequest, PurchasedResponse
from dto.Transaction import TransactionUpdateRequest
from service.TransactionServices import get_transaction_service,update_transaction_service
from service.ProductService import get_product_service
from model import Purchased

def delete_purchase_service(session: Session, id) -> bool:
    product = session.query(Purchased).get(id)
    session.delete(product)
    session.commit()
    session.refresh(product)
    return product is None

def create_purchase_service(session: Session, request: PurchasedRequest) -> PurchasedResponse:
    purchase = Purchased(**request.dict())
    session.add(purchase)
    session.commit()
    session.refresh(purchase)

    return PurchasedResponse(**purchase.dict())

def get_purchaseds_service(session: Session) -> list[PurchasedResponse]:
    products = session.query(Purchased).all()
    return [PurchasedResponse(**product.dict()) for product in products]

def get_purchase_service(session: Session, id) -> PurchasedResponse:
    product = session.query(Purchased).get(id)
    return PurchasedResponse(**product.dict()) if product else None
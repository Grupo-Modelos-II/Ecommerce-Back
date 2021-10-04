from sqlalchemy.orm import Session

from dto.Purchased import PurchasedRequest, PurchasedResponse

from model import Purchased

def delete_purchase_service(session: Session, id) -> bool:
    product = session.query(Purchased).get(id)
    session.delete(product)
    session.commit()
    session.refresh(product)
    return product is None

def create_purchase_service(session: Session, request: PurchasedRequest) -> PurchasedResponse:
    product = Purchased(**request.dict())
    session.add(product)
    session.commit()
    return PurchasedResponse(**product.to_dict())

def get_purchaseds_service(session: Session) -> list[PurchasedResponse]:
    products = session.query(Purchased).all()
    return [PurchasedResponse(**product.to_dict()) for product in products]

def get_purchase_service(session: Session, id) -> PurchasedResponse:
    product = session.query(Purchased).get(id)
    return PurchasedResponse(**product.to_dict()) if product else None
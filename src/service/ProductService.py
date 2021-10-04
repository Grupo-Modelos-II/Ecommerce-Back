from sqlalchemy.orm import Session

from dto.Product import ProductRequest, ProductResponse

from model import Product

def delete_product_service(session: Session, id) -> bool:
    product = session.query(Product).get(id)
    session.delete(product)
    session.commit()
    session.refresh(product)
    return product is None

def create_product_service(session: Session, request: ProductRequest) -> ProductResponse:
    product = Product(**request.dict())
    session.add(product)
    session.commit()
    session.refresh(product)
    return ProductResponse(**product.to_dict())

def get_products_service(session: Session) -> list[ProductResponse]:
    products = session.query(Product).all()
    return [ProductResponse(**product.to_dict()) for product in products]

def get_product_service(session: Session, id) -> ProductResponse:
    product = session.query(Product).get(id)
    return ProductResponse(**product.to_dict()) if product else None
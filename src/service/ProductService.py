from sqlalchemy.orm import Session

from dto.Product import ProductRequest, ProductResponse

from service.StorageService import get_file_url_service, get_list_file_url_service

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
    return set_product_media_information_service(ProductResponse(**product.dict()))

def get_products_service(session: Session) -> list[ProductResponse]:
    products = session.query(Product).all()
    return [set_product_media_information_service(ProductResponse(**product.dict())) for product in products]

def get_product_service(session: Session, id) -> ProductResponse:
    product = session.query(Product).get(id)
    return set_product_media_information_service(ProductResponse(**product.dict())) if product else None

def set_product_media_information_service(product: ProductResponse) -> ProductResponse:
    product.mainImage = get_file_url_service(f'product/{product.id}')
    product.images = get_list_file_url_service(f'product/{product.id}')
    return product
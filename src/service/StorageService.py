from tempfile import SpooledTemporaryFile
from sqlalchemy.orm import Session

from config.firebaseConfig import get_storage_client

from .ProductService import get_product_service

from model import Product_Image
from model.Product import Product

def upload_main_file_service(file: SpooledTemporaryFile, destination: str, content_type: str, session: Session, id: str) -> str:
    product = session.query(Product).get(id)
    bucket = get_storage_client()
    blob = bucket.blob(destination)
    blob.upload_from_file(file, content_type = content_type)
    blob.make_public()
    product.mainImage = blob.public_url
    session.flush()
    session.commit()
    session.refresh(product)
    return blob.public_url

def upload_file_service(file: SpooledTemporaryFile, destination: str, content_type: str, session: Session, id: str) -> str:
    bucket = get_storage_client()
    blob = bucket.blob(destination)
    blob.upload_from_file(file, content_type = content_type)
    blob.make_public()
    product_image = Product_Image(id_product = id, image = blob.public_url)
    session.add(product_image)
    session.commit()
    session.refresh(product_image)
    return blob.public_url
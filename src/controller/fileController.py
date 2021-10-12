from fastapi import Depends, APIRouter, Response, File, UploadFile
from fastapi_router_controller import Controller
from sqlalchemy.orm import Session
from service.ProductService import get_product_service
from service.StorageService import upload_main_file_service, upload_file_service
from config.databaseConfig import get_db

router = APIRouter(prefix='/file')
controller = Controller(router)

@controller.resource()
class FileController:

    @controller.route.post("/product/upload", summary="Upload Product Image")
    def upload_product_image(self, id: str, file: UploadFile = File(...), session: Session = Depends(get_db)):
        if get_product_service(session, id) is not None:
            return Response(status_code=200, content=upload_file_service(file.file, f'product/{id}/images/{file.filename}', file.content_type, session, id))
        else:
            return Response(status_code=404, content="Product not found")

    @controller.route.post("/product/upload/main", summary="Upload Main Product Image")
    def upload_product_image(self, id: str, file: UploadFile = File(...), session: Session = Depends(get_db)):
        if get_product_service(session, id) is not None:
            return Response(status_code=200, content=upload_main_file_service(file.file, f'product/{id}/{file.filename}', file.content_type, session, id))
        else:
            return Response(status_code=404, content="Product not found")
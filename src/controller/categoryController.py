from fastapi import Depends, APIRouter, Response
from fastapi_router_controller import Controller
from sqlalchemy.orm import Session
from service.CategoryService import get_categories_service, get_category_service, create_category_service, delete_category_service
from config.databaseConfig import get_db
from dto.Category import CategoryRequest, CategoryResponse
from config.securityConfig import auth_scheme
from security.middlewares.AuthMiddleware import AuthMiddleware

routerProduct = APIRouter(prefix='/product')
productControllerRest = Controller(routerProduct)

@productControllerRest.resource()
class ProductController:

    @productControllerRest.route.get("/", summary="Get All Products", response_model=list[ProductResponse])
    def get_all_products(self, session: Session = Depends(get_db)) -> list[ProductResponse]:
        return get_categories_service(session)

    @productControllerRest.route.get("/{id}",summary="Get Specific Product", response_model=ProductResponse)
    def get_product(self, response: Response, id: str, session: Session = Depends(get_db)) -> ProductResponse:
        product = get_category_service(session, id)
        if product is None:
            response.status_code = 404
        return product

    @productControllerRest.route.post('/',summary="Creation of a Product",response_model=ProductResponse)
    def create_product(self,category: ProductRequest, session: Session = Depends(get_db)) -> ProductResponse:
        return create_category_service(session, category)

    @productControllerRest.route.delete('/{id}',summary="Delete Data Product", response_model=bool)
    def delete_client(self, id, session: Session = Depends(get_db), token: str = Depends(auth_scheme)) -> bool:
        isValidToken = AuthMiddleware.hasNotExpired(token)
        if isValidToken:
            return delete_category_service(session, id)
        return False

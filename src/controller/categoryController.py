from fastapi import Depends, APIRouter, Response
from fastapi_router_controller import Controller
from sqlalchemy.orm import Session
from service.CategoryService import get_categories_service, get_category_service, create_category_service, delete_category_service
from config.databaseConfig import get_db
from dto.Category import CategoryRequest, CategoryResponse
from config.securityConfig import auth_scheme
from security.middlewares.AuthMiddleware import AuthMiddleware

routerCategory = APIRouter(prefix='/product')
categoryControllerRest = Controller(routerCategory)
@categoryControllerRest.resource()
class CategoryController:

    @categoryControllerRest.route.get("/", summary="Get All Categories", response_model=list[CategoryResponse])
    def get_all_products(self, session: Session = Depends(get_db)) -> list[CategoryResponse]:
        return get_categories_service(session)

    @categoryControllerRest.route.get("/{id}",summary="Get Specific Category", response_model=CategoryResponse)
    def get_product(self, response: Response, id: str, session: Session = Depends(get_db)) -> CategoryResponse:
        product = get_category_service(session, id)
        if product is None:
            response.status_code = 404
        return product

    @categoryControllerRest.route.post('/',summary="Creation of a Category",response_model=CategoryResponse)
    def create_product(self,category: CategoryRequest, session: Session = Depends(get_db)) -> CategoryResponse:
        return create_category_service(session, category)

    @categoryControllerRest.route.delete('/{id}',summary="Delete Data Category", response_model=bool)
    def delete_client(self, id, session: Session = Depends(get_db), token: str = Depends(auth_scheme)) -> bool:
        isValidToken = AuthMiddleware.hasNotExpired(token)
        if isValidToken:
            return delete_category_service(session, id)
        return False

from fastapi import Depends, APIRouter, Response
from fastapi_router_controller import Controller
from sqlalchemy.orm import Session
from service.PurchasedService import get_purchaseds_service, get_purchase_service, create_purchase_service, delete_purchase_service
from config.databaseConfig import get_db
from dto.Purchased import PurchasedRequest, PurchasedResponse
from config.securityConfig import auth_scheme
from security.middlewares.AuthMiddleware import AuthMiddleware

router = APIRouter(prefix='/purchase')
controller = Controller(router)

@controller.resource()
class PurchaseController:

    @controller.route.get("/", summary="Get All Purchases", response_model=list[PurchasedResponse])
    def get_all_purchases(self, session: Session = Depends(get_db)) -> list[PurchasedResponse]:
        return get_purchaseds_service(session)

    @controller.route.get("/{id}",summary="Get Specific Purchase", response_model=PurchasedResponse)
    def get_purchase(self, response: Response, id: str, session: Session = Depends(get_db)) -> PurchasedResponse:
        product = get_purchase_service(session, id)
        if product is None:
            response.status_code = 404
        return product

    @controller.route.post('/',summary="Creation of a Purchase",response_model=PurchasedResponse)
    def create_purchase(self,purchase: PurchasedRequest, session: Session = Depends(get_db)) -> PurchasedResponse:
        
        return create_purchase_service(session, purchase)

    @controller.route.delete('/{id}',summary="Delete Data Purchase", response_model=bool)
    def delete_purchase(self, id, session: Session = Depends(get_db), token: str = Depends(auth_scheme)) -> bool:
        isValidToken = AuthMiddleware.enabledToken(token,session)
        if isValidToken:
            return delete_purchase_service(session, id)
        return False

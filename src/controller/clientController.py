from fastapi import Depends, APIRouter, Response
from fastapi_router_controller import Controller
from sqlalchemy.orm import Session
from service.ClientService import get_clients_service, get_client_service, create_client_service, delete_client_service, update_client_service
from config.databaseConfig import get_db
from dto.Client import ClientRequest, ClientResponse, ClientUpdateRequest
from security.authSecurity import crypt_password

from security.middlewares.AuthMiddleware import AuthMiddleware

from config.securityConfig import auth_scheme

from security.middlewares.AuthMiddleware import AuthMiddleware

routerClient = APIRouter(prefix='/client')
clientControllerRest = Controller(routerClient)

@clientControllerRest.resource()
class ClientController:

    @clientControllerRest.route.get("/", summary="Get All Clients", response_model=list[ClientResponse])
    def get_all_clients(self, response: Response, session: Session = Depends(get_db), token: str = Depends(auth_scheme)) -> list[ClientResponse]:
        isValidToken = AuthMiddleware.enabledToken(token,session)
        if not isValidToken:
            response.status_code = 401
            return []
        return get_clients_service(session)

    @clientControllerRest.route.get("/{id}",summary="Get Specific Client", response_model=ClientResponse)
    def get_client(self, response: Response, id: str, session: Session = Depends(get_db), token: str = Depends(auth_scheme)) -> ClientResponse:
        isValidToken = AuthMiddleware.enabledToken(token,session)
        if not isValidToken:
            response.status_code = 401
            return None
        client = get_client_service(session, id)
        if client is None:
            response.status_code = 404
        return client

    @clientControllerRest.route.post('/',summary="Creation of a Client",response_model=ClientResponse)
    def create_client(self,client: ClientRequest, session: Session = Depends(get_db)) -> ClientResponse:
        client.password = crypt_password(client.password)
        return create_client_service(session, client)

    @clientControllerRest.route.put('/', summary="Update Client values", response_model=ClientResponse)
    def update_client(self, client: ClientUpdateRequest, session: Session = Depends(get_db)) -> ClientResponse:
        return update_client_service(session, client)

    @clientControllerRest.route.delete('/{id}',summary="Delete Data Client", response_model=bool)
    def delete_client(self, id, session: Session = Depends(get_db), token: str = Depends(auth_scheme)) -> bool:
        isValidToken = AuthMiddleware.enabledToken(token,session)
        if isValidToken:
            return delete_client_service(session, id)
        return False

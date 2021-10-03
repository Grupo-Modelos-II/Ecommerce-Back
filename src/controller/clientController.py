from fastapi import Depends,APIRouter
from fastapi_router_controller import Controller
from sqlalchemy.orm import Session
from service.ClientService import get_clients_service, get_client_service, create_client_service, delete_client_service
from config.databaseConfig import get_db
from dto.Client import ClientRequest, ClientResponse
from security.authSecurity import crypt_password

routerClient = APIRouter(prefix='/client')
clientControllerRest = Controller(routerClient)

@clientControllerRest.resource()
class ClientController:

    @clientControllerRest.route.get("/", summary="Get All Clients", response_model=list[ClientResponse])
    def get_all_clients(self,session: Session = Depends(get_db)):
        return get_clients_service(session)

    @clientControllerRest.route.get("/{id}",summary="Get Specific Client", response_model=ClientResponse)
    def get_client(self,id, session: Session = Depends(get_db)):
        return get_client_service(session, id)

    @clientControllerRest.route.post('/',summary="Creation of a Client",response_model=ClientResponse)
    def create_client(self,client: ClientRequest, session: Session = Depends(get_db)):
        client.password = crypt_password(client.password)
        return create_client_service(session, client)

    @clientControllerRest.route.delete('/{id}',summary="Delete Data Client", response_model=None)
    def delete_client(self,id, session: Session = Depends(get_db)):
        delete_client_service(session, id)
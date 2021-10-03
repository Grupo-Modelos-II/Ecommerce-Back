from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from service.ClientService import get_clients_service, get_client_service, create_client_service, delete_client_service
from config.databaseConfig import get_db
from dto.Client import ClientRequest, ClientResponse
from security.authSecurity import crypt_password

clientController = APIRouter(prefix='/client')

@clientController.get('/', response_model=list[ClientResponse])
def get_all_clients(session: Session = Depends(get_db)) -> list[ClientResponse]:
    return get_clients_service(session)

@clientController.get('/test/hash', response_model=str)
def test(password: str) -> str:
    return crypt_password(password)

@clientController.get('/{id}', response_model=ClientResponse)
def get_client(id, session: Session = Depends(get_db)) -> ClientResponse:
    return get_client_service(session, id)

@clientController.post('/', response_model=ClientResponse)
def create_client(client: ClientRequest, session: Session = Depends(get_db)) -> ClientResponse:
    return create_client_service(session, client)

@clientController.delete('/{id}', response_model=None)
def delete_client(id, session: Session = Depends(get_db)) -> None:
    delete_client_service(session, id)
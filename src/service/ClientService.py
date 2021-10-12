from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import Update

from dto.Client import ClientRequest, ClientResponse, ClientUpdateRequest

from model import Client

def delete_client_service(session: Session, id) -> bool:
    client = session.query(Client).get(id)
    session.delete(client)
    session.commit()
    session.refresh(client)
    return client is None

def update_client_service(session: Session, request: ClientUpdateRequest) -> ClientResponse:
    client = session.query(Client).get(request.id)
    client.update(**request.dict())
    session.flush()
    session.commit()
    session.refresh(client)
    return ClientResponse(**client.dict())

def create_client_service(session: Session, request: ClientRequest) -> ClientResponse:
    client = Client(**request.dict())
    session.add(client)
    session.commit()
    session.refresh(client)
    return ClientResponse(**client.dict())
    
def get_clients_service(session: Session) -> list[ClientResponse]:
    clients = session.query(Client).all()
    return [ClientResponse(**client.dict()) for client in clients]

def get_client_service(session: Session, id) -> ClientResponse:
    client = session.query(Client).get(id)
    return ClientResponse(**client.dict()) if client else None

def get_client_by_email(session:Session,email:str) -> ClientResponse:
    client = session.query(Client).filter(Client.email == email).first()
    return ClientResponse(**client.dict()) if client else None

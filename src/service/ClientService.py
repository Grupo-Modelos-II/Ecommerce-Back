from sqlalchemy.orm import Session

from dto.Client import ClientRequest, ClientResponse

from model import Client

def delete_client_service(session: Session, id) -> None:
    client = session.query(Client).get(id)
    print(client)
    session.delete(client)
    session.commit()

def create_client_service(session: Session, request: ClientRequest) -> ClientResponse:
    client = Client(**request.dict())
    session.add(client)
    session.commit()
    return ClientResponse(**client.to_dict())
    
def get_clients_service(session: Session) -> list:
    clients = session.query(Client).all()
    return ClientResponse(**client.to_dict())

def get_client_service(session: Session, id) -> ClientResponse:
    client = session.query(Client).get(id)
    return ClientResponse(**client.to_dict())

def get_client_by_email(session:Session,email:str) -> ClientResponse:
    client = session.query(Client).filter(Client.email == email).first()
    return ClientResponse(**client.to_dict())

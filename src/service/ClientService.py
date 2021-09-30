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
    return ClientResponse(id = client.id, name = client.name, email = client.email, identifier_type = client.identifier_type, identifier = client.identifier, location = client.location, credits = client.credits)

def get_clients_service(session: Session) -> list:
    clients = session.query(Client).all()
    return [ClientResponse(id = client.id, name = client.name, email = client.email, identifier_type = client.identifier_type, identifier = client.identifier, location = client.location, credits = client.credits) for client in clients]

def get_client_service(session: Session, id) -> ClientResponse:
    client = session.query(Client).get(id)
    return ClientResponse(id = client.id, name = client.name, email = client.email, identifier_type = client.identifier_type, identifier = client.identifier, location = client.location, credits = client.credits)
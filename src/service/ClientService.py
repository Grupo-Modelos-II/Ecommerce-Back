from sqlalchemy.orm import Session

from model import Client

def delete_client_service(session: Session, id):
    client = session.query(Client).get(id)
    session.delete(client)
    session.commit()
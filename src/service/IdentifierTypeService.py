from uuid import uuid4

from sqlalchemy.orm import Session

from dto.IdentifierType import IdentifierTypeRequest, IdentifierTypeResponse

from model import Identifier_Type

def delete_identifier_type_service(session: Session, id):
    identifierType = session.query(identifierType).get(id)
    session.delete(identifierType)
    session.commit()

def create_identifier_type_service(session: Session, request: IdentifierTypeRequest) -> IdentifierTypeResponse:
    identifierType = Identifier_Type(name = request.name)
    session.add(identifierType)
    session.commit()
    return IdentifierTypeResponse(id = identifierType.id, name = identifierType.name)

def get_identifier_types_service(session: Session):
    return session.query(Identifier_Type).all()

def get_identifier_type_service(session: Session, id):
    identifierType = session.query(Identifier_Type).get(id)
    return identifierType
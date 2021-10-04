from sqlalchemy.orm import Session

from dto.IdentifierType import IdentifierTypeRequest, IdentifierTypeResponse

from model import Identifier_Type

def delete_identifier_type_service(session: Session, id) -> bool:
    identifierType = session.query(Identifier_Type).get(id)
    session.delete(identifierType)
    session.commit()
    session.refresh(identifierType)
    return identifierType is None

def create_identifier_type_service(session: Session, request: IdentifierTypeRequest) -> IdentifierTypeResponse:
    identifierType = Identifier_Type(**request.dict())
    session.add(identifierType)
    session.commit()
    session.refresh(identifierType)
    return IdentifierTypeResponse(**identifierType.to_dict())

def get_identifier_types_service(session: Session) -> list[IdentifierTypeResponse]:
    identifierTypes = session.query(Identifier_Type).all()
    return [IdentifierTypeResponse(**identifierType.to_dict()) for identifierType in identifierTypes]

def get_identifier_type_service(session: Session, id) -> IdentifierTypeResponse:
    identifierType = session.query(Identifier_Type).get(id)
    return IdentifierTypeResponse(**identifierType.to_dict()) if identifierType else None
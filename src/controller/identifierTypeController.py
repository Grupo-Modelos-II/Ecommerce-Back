from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from config.databaseConfig import get_db

from dto.IdentifierType import IdentifierTypeRequest, IdentifierTypeResponse

from service.IdentifierTypeService import get_identifier_type_service, get_identifier_types_service, create_identifier_type_service, delete_identifier_type_service

identifierTypeController = APIRouter(prefix='/identifier-type')

@identifierTypeController.get('/{id}')
def get_identifier_type(id, session: Session = Depends(get_db)):
    return get_identifier_type_service(session, id)

@identifierTypeController.get('/')
def get_all_identifier_types(session: Session = Depends(get_db)):
    return get_identifier_types_service(session)

@identifierTypeController.post('/save', response_model=IdentifierTypeResponse)
def create_identifier_type(identifierType: IdentifierTypeRequest, session: Session = Depends(get_db)):
    return create_identifier_type_service(session, identifierType)

@identifierTypeController.delete('/{id}')
def delete_identifier_type(id, session: Session = Depends(get_db)):
    return delete_identifier_type_service(session, id)
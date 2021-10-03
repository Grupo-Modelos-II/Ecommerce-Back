from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi_router_controller import Controller

from config.databaseConfig import get_db

from dto.IdentifierType import IdentifierTypeRequest, IdentifierTypeResponse

from service.IdentifierTypeService import get_identifier_type_service, get_identifier_types_service, create_identifier_type_service, delete_identifier_type_service

routerIdentifierType = APIRouter(prefix='/identifier-type')
identifierTypeControllerRest = Controller(routerIdentifierType)

@identifierTypeControllerRest.resource()
class identifierTypeController:
    @identifierTypeControllerRest.route.get('/{id}', summary="Get Specific Identifier Type", response_model=IdentifierTypeResponse)
    def get_identifier_type(self, id: int, db: Session = Depends(get_db)):
        return get_identifier_type_service(db, id)

    @identifierTypeControllerRest.route.get('/', summary="Get All Identifier Types", response_model=list[IdentifierTypeResponse])
    def get_identifier_types(self, db: Session = Depends(get_db)):
        return get_identifier_types_service(db)

    @identifierTypeControllerRest.route.post('/', summary="Creation of a Identifier Type", response_model=IdentifierTypeResponse)
    def create_identifier_type(self, identifierType: IdentifierTypeRequest, db: Session = Depends(get_db)):
        return create_identifier_type_service(db, identifierType)

    @identifierTypeControllerRest.route.delete('/{identifierTypeId}', summary="Delete Identifier Type", response_model=None)
    def delete_identifier_type(self, identifierTypeId: int, db: Session = Depends(get_db)):
        return delete_identifier_type_service(db, identifierTypeId)
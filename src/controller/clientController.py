from fastapi import APIRouter

from service.ClientService import delete_client_service

clientController = APIRouter(prefix='/clients')

@clientController.get('/')
def get_all_clients():
    pass

@clientController.get('/{id}')
def get_client(id):
    pass

@clientController.post('/save')
def create_client(client):
    pass

@clientController.delete('/{id}')
def delete_client(id):
    pass
from controller.clientController import clientController
from controller.identifierTypeController import identifierTypeController
from .databaseConfig import init_db

def init_app(server):
    #handle routes for Api
    server.include_router(clientController)
    server.include_router(identifierTypeController)
    init_db()
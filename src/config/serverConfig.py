from controller.clientController import ClientController
from controller.authController import AuthController
from controller.identifierTypeController import identifierTypeController
from .databaseConfig import init_db

def init_app(server):
    #handle routes for Api
    server.include_router(ClientController.router())
    server.include_router(AuthController.router())
    server.include_router(identifierTypeController)
    init_db()
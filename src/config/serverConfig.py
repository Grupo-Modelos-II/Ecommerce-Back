from controller.userController import userController
from .databaseConfig import init_db, get_db

def init_app(server):
    #handle routes for Api
    server.include_router(userController)
    init_db()
    db = get_db()
from controller.clientController import ClientController
from controller.authController import AuthController
from controller.identifierTypeController import identifierTypeController
from controller.productController import ProductController
from controller.purchasedController import PurchaseController
from controller.categoryController import CategoryController
from controller.transactionController import TransactionController
from .databaseConfig import init_db

def init_app(server):
    #handle routes for Api
    server.include_router(ClientController.router())
    server.include_router(AuthController.router())
    server.include_router(identifierTypeController.router())
    server.include_router(ProductController.router())
    server.include_router(CategoryController.router())
    server.include_router(PurchaseController.router())
    server.include_router(TransactionController.router())
    init_db()
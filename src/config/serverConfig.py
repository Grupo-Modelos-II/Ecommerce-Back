from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controller.clientController import ClientController
from controller.authController import AuthController
from controller.identifierTypeController import identifierTypeController
from controller.productController import ProductController
from controller.purchasedController import PurchaseController
from controller.categoryController import CategoryController
from controller.transactionController import TransactionController
from controller.fileController import FileController

from .databaseConfig import init_db

from .firebaseConfig import init_firebase

def _set_cors(server: FastAPI):
    server.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def init_app(server: FastAPI):
    #handle routes for Api
    server.include_router(ClientController.router())
    server.include_router(AuthController.router())
    server.include_router(identifierTypeController.router())
    server.include_router(ProductController.router())
    server.include_router(CategoryController.router())
    server.include_router(PurchaseController.router())
    server.include_router(TransactionController.router())
    server.include_router(FileController.router())
    #generate cors for server
    _set_cors(server)

    #create database tables
    init_db()

    #initialize firebase
    init_firebase()
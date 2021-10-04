from fastapi import Depends, APIRouter, Response
from fastapi_router_controller import Controller
from sqlalchemy.orm import Session
from service.TransactionServices import get_transactions_service, get_transaction_service, create_transaction_service, get_transaction_by_id_client_service
from config.databaseConfig import get_db
from dto.Transaction import TransactionRequest, TransactionResponse
from config.securityConfig import auth_scheme
from security.middlewares.AuthMiddleware import AuthMiddleware

routerTransaction = APIRouter(prefix='/transaction')
transactionControllerRest = Controller(routerTransaction)

@transactionControllerRest.resource()
class TransactionController:

    @transactionControllerRest.route.get("/", summary="Get All Transactions", response_model=list[TransactionResponse])
    def get_all_transactions(self, response: Response, session: Session = Depends(get_db), token: str = Depends(auth_scheme)) -> list[TransactionResponse]:
        isValidToken = AuthMiddleware.hasNotExpired(token)
        if not isValidToken:
            response.status_code = 401
            return []
        return get_transactions_service(session)

    @transactionControllerRest.route.get("/{id}",summary="Get Specific Transaction", response_model=TransactionResponse)
    def get_transaction(self, response: Response, id: str, session: Session = Depends(get_db), token: str = Depends(auth_scheme)) -> TransactionResponse:
        isValidToken = AuthMiddleware.hasNotExpired(token)
        if not isValidToken:
            response.status_code = 401
            return None
        transaction = get_transaction_service(session, id)
        if transaction is None:
            response.status_code = 404
        return transaction

    @transactionControllerRest.route.get("/client/{id}", summary="Get All Transactions By Client", response_model=list[TransactionResponse])
    def get_transactions_by_client(self, response: Response, id: str, session: Session = Depends(get_db), token: str = Depends(auth_scheme)) -> list[TransactionResponse]:
        isValidToken = AuthMiddleware.hasNotExpired(token)
        if not isValidToken:
            response.status_code = 401
            return []
        transactions = get_transaction_by_id_client_service(session, id)
        return transactions

    @transactionControllerRest.route.post('/',summary="Creation of a Transaction",response_model=TransactionResponse)
    def create_transaction(self, response: Response, transaction: TransactionRequest, session: Session = Depends(get_db), token: str = Depends(auth_scheme)) -> TransactionResponse:
        isValidToken = AuthMiddleware.hasNotExpired(token)
        if not isValidToken:
            response.status_code = 401
            return None
        return create_transaction_service(session, transaction)
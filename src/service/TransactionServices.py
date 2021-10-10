from sqlalchemy.orm import Session

from dto.Transaction import TransactionRequest, TransactionResponse,TransactionUpdateRequest

from model import Transaction

def create_transaction_service(session: Session, request: TransactionRequest) -> TransactionResponse:
    transaction = Transaction(**request.dict())
    session.add(transaction)
    session.commit()
    session.refresh(transaction)
    return TransactionResponse(**transaction.dict())

def get_transactions_service(session: Session) -> list[TransactionResponse]:
    transactions = session.query(Transaction).all()
    return [TransactionResponse(**transaction.dict()) for transaction in transactions]

def get_transaction_service(session: Session, id) -> TransactionResponse:
    transaction = session.query(Transaction).get(id)
    return TransactionResponse(**transaction.dict()) if transaction else None

def get_transaction_by_id_client_service(session: Session, id_client) -> list[TransactionResponse]:
    transactions = session.query(Transaction).filter(Transaction.id_client == id_client).all()
    return [TransactionResponse(**transaction.dict()) for transaction in transactions]

def update_transaction_service(session:Session,request:TransactionUpdateRequest) -> TransactionResponse:
    transaction = session.query(Transaction).get(request.id)
    transaction.update(**request.dict())
    session.flush()
    session.commit()
    session.refresh(transaction)
    return TransactionResponse(**transaction.dict())
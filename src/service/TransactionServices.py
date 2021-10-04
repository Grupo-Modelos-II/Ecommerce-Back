from sqlalchemy.orm import Session

from dto.Transaction import TransactionRequest, TransactionResponse

from model import Transaction

def create_transaction_service(session: Session, request: TransactionRequest) -> TransactionResponse:
    transaction = Transaction(**request.dict())
    session.add(transaction)
    session.commit()
    session.refresh(transaction)
    return TransactionResponse(**transaction.to_dict())

def get_transactions_service(session: Session) -> list[TransactionResponse]:
    transactions = session.query(Transaction).all()
    return [TransactionResponse(**transaction.to_dict()) for transaction in transactions]

def get_transaction_service(session: Session, id) -> TransactionResponse:
    transaction = session.query(Transaction).get(id)
    return TransactionResponse(**transaction.to_dict()) if transaction else None

def get_transaction_by_id_client_service(session: Session, id_client) -> list[TransactionResponse]:
    transactions = session.query(Transaction).filter(Transaction.id_client == id_client).all()
    return [TransactionResponse(**transaction.to_dict()) for transaction in transactions]
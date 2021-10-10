from security.authSecurity import get_payload
from sqlalchemy.orm import Session
from time import time
from config.databaseConfig import get_db
from service.ClientService import get_client_service
class AuthMiddleware:
    
    @classmethod
    def _isValidToken(cls, token: str) -> bool:
        payload = get_payload(token)
        return payload is not None
    
    @classmethod
    def _hasNotExpired(cls, token: str) -> bool:
        if cls._isValidToken(token):
            payload = get_payload(token)
            return payload['exp'] > time()
        return False

    @classmethod
    def _isValidUser(cls,token:str,session:Session) -> bool:
        if cls._hasNotExpired(token):
            payload = get_payload(token)
            id_client = payload['id_client']
            return get_client_service(session,id_client) is not None

    @classmethod
    def enabledToken(cls,token:str,session:Session) -> bool:
        return cls._isValidUser(token,session)

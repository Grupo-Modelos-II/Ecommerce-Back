from security.authSecurity import get_payload
from time import time

class AuthMiddleware:
    
    @classmethod
    def _isValidToken(cls, token: str) -> bool:
        payload = get_payload(token)
        return payload is not None
    
    @classmethod
    def hasNotExpired(cls, token: str) -> bool:
        if cls._isValidToken(token):
            payload = get_payload(token)
            return payload['exp'] > time()
        return False
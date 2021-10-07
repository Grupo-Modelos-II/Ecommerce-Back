from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from config.databaseConfig import get_db
from fastapi_router_controller import Controller
from dto.Auth import AuthRequest
from security.authSecurity import sign_token,verify_password
from service.ClientService import get_client_by_email

router = APIRouter(prefix='/auth')
controller = Controller(router)

@controller.resource()
class AuthController:

    @controller.route.post("/login",summary="Get All Clients", response_model=dict)
    def login_user(self,authData:AuthRequest,session: Session = Depends(get_db)):
        userData = get_client_by_email(session,authData.email)
        verifiedData = False if (not userData) else verify_password(userData.password,authData.password)
        if verifiedData:
            token = sign_token({'id_client':userData.id})
            return {'token':token}
        else:
            return {'message':'Nombre de usuario y/o contraseña incorrectos'}
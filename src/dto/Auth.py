from pydantic import BaseModel

class AuthRequest(BaseModel):
    email: str
    password: str

    def __str__(self):
        return 'email:{} \n password:{}'.format(self.email,self.password)
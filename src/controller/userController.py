from fastapi import APIRouter

userController = APIRouter()

@userController.get('/users')
def get_all_users():
    return [
        {'name':'Sergio','age':19},
        {'name':'Jesus','age':20},
    ]
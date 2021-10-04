from jwt import decode,encode
from util.hash import mix_password
from random import randint
from os import getenv

from time import time

def sign_token(data_payload):
    return encode({**data_payload, "exp": int(time()) + int(getenv("EXPIRATION_TIME"))},getenv('SECRET'), algorithm=str(getenv('ALGORITHM')))

def get_payload(token):
    return decode(token, getenv('SECRET'), algorithms=[str(getenv('ALGORITHM'))],options={"verify_exp": False})

def crypt_password(password):
    return mix_password(password,getenv('SECRET_HASH'))

def verify_password(hash_password,password):
    return hash_password == crypt_password(password)
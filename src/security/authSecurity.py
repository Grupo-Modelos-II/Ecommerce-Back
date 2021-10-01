from jwt import decode,encode
from util.hash import cipher,decrypt
from random import randint
from os import getenv

def sign_token(data_payload):
    return encode(data_payload,getenv('SECRET'),algorithm=str(getenv('ALGORITHM')))

def get_payload(token):
    return decode(token, getenv('SECRET'), algorithms=[str(getenv('ALGORITHM'))],options={"verify_exp": False})

def exchange(password,secret):
    pass


def crypt_password(password):
    return cipher(password,len(password)%26)

def verify_password(hash_password,password):
    return decrypt(hash_password) == password
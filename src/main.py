from fastapi import FastAPI
from config.serverConfig import init_app

server = FastAPI()

if __name__ == 'main':
    init_app(server)
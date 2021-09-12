from fastapi import FastAPI
from config.globalConfig import init_app

server = FastAPI()
init_app(server)
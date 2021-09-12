#!/bin/bash

#Variables a utilizar

option=$1
port=0

#Logica del script
function set_env(){
    if  [ ! -d ./env ]
    then
        python3 -m venv env
    fi
    source env/bin/activate
    pip install -r requirements.txt
}

function set_port(){
    if [ -f .env ]
    then
        cat .env | export
        port=$PORT
    else
        port=3000
    fi
}

function start_service(){
    cd src
    if [ $option = "dev" ]
    then
        uvicorn main:server --reload --port=$port
    elif [ $option = "prod" ]
    then
        uvicorn main:server --port=$PORT
    else
        echo -e "\nIngrese una opción valida para ejecutar la aplicación\n"
    fi
}

clear

set_env

set_port

start_service

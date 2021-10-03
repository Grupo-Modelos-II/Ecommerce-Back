# Especificar que imagen se va a usar por paso
FROM python:latest
WORKDIR /app  
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src .
ENTRYPOINT [ "uvicorn" ]
CMD [ "main:server","--port=$PORT" ]
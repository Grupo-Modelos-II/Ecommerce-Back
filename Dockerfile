# Especificar que imagen se va a usar por paso
FROM python:latest
WORKDIR /app  
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src .
ENTRYPOINT [ "uvicorn" ]
CMD [ "main:server","--host", "0.0.0.0", "--port", "5000" ]
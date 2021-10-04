from uuid import uuid4

from config.databaseConfig import Base

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, BigInteger

class Identifier_Type(Base):
    __tablename__ = 'Identifier_Type'
    id = Column(String, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)

    clients = relationship("Client", back_populates="identifier_type")

    def __init__(self, **kwargs):
        self.id = str(uuid4())
        self.name = kwargs["name"]

    def to_dict(self):
        return {'id':self.id,'name':self.name,'clients':self.clients}

class Client(Base):
    __tablename__ = 'Client'
    id = Column(String, primary_key=True)
    id_identifier_type = Column(String, ForeignKey('Identifier_Type.id'), nullable=False)
    identifier = Column(String, unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255),nullable=False)
    location = Column(String(255), nullable=False)
    credits = Column(BigInteger, nullable=False)

    identifier_type = relationship("Identifier_Type", back_populates="clients")
    transactions = relationship("Transaction", back_populates="client")

    def __init__(self, **kwargs):
        self.id = str(uuid4())
        self.id_identifier_type = kwargs["id_identifier_type"]
        self.identifier = kwargs["identifier"]
        self.name = kwargs["name"]
        self.email = kwargs["email"]
        self.password = kwargs["password"]
        self.location = kwargs["location"]
        self.credits = kwargs["credits"]

    def to_dict(self):
        return {
            'id':self.id,
            'id_identifier_type':self.id_identifier_type,
            'identifier':self.identifier,
            'name':self.name,
            'email':self.email,
            'password':self.password,
            'location':self.location,
            'credits':self.credits,
            'identifier_type':self.identifier_type,
            'transactions':self.transactions
        }

    def update(self, **kwargs):
        self.id_identifier_type = kwargs["id_identifier_type"] or self.id_identifier_type
        self.identifier = kwargs["identifier"] or self.identifier
        self.name = kwargs["name"] or self.name
        self.email = kwargs["email"] or self.email
        self.password = kwargs["password"] or self.password
        self.location = kwargs["location"] or self.location
        self.credits = kwargs["credits"] or self.credits
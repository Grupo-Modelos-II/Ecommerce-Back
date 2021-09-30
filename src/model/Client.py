from uuid import uuid4

from config.databaseConfig import Base

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, BigInteger

class Identifier_Type(Base):
    __tablename__ = 'Identifier_Type'
    id = Column(String, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)

    def __init__(self, **kwargs):
        self.id = str(uuid4())
        self.name = kwargs["name"]

class Client(Base):
    __tablename__ = 'Client'
    id = Column(String, primary_key=True)
    id_identifier_type = Column(String, ForeignKey('Identifier_Type.id'), nullable=False)
    identifier = Column(BigInteger, unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    location = Column(String(255), nullable=False)
    credits = Column(BigInteger, nullable=False)

    transactions = relationship("Transaction", back_populates="clients")
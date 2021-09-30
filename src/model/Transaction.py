from datetime import datetime

from config.databaseConfig import Base

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, BigInteger, Date

class Transaction(Base):
    __tablename__ = 'Transaction'
    id = Column(String, primary_key=True)
    id_client = Column(String, ForeignKey('Client.id'), nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.now)
    total = Column(BigInteger, nullable=False)

    clients = relationship('Client', back_populates='transactions')
    purchases = relationship('Purchased', back_populates='transactions')

class Purchased(Base):
    __tablename__ = 'Purchased'
    id = Column(String, primary_key=True)
    id_transaction = Column(String, ForeignKey('Transaction.id'), nullable=False)
    id_product = Column(String, ForeignKey('Product.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    cost = Column(BigInteger, nullable=False)
    has_variations = Column(Boolean, nullable=False, default=False)

    transactions = relationship('Transaction', back_populates='purchases')
    purchased_variations = relationship('Purchased_Variation', back_populates='purchases')

class Purchased_Variation(Base):
    __tablename__ = 'Purchased_Variation'
    id_purchased = Column(String, ForeignKey('Purchased.id'), primary_key=True)
    id_variation = Column(String, ForeignKey('Product_Variation.id'), primary_key=True)

    purchases = relationship('Purchased', back_populates='purchased_variations')
    products_variations = relationship('Product_Variation', back_populates='purchased_variations')